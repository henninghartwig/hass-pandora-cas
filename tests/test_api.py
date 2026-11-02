"""Check endpoint routing against the pinned pandora-cas client, without network."""

import importlib.util
from pathlib import Path
import unittest
from unittest.mock import MagicMock, AsyncMock

from pandora_cas.account import PandoraOnlineAccount as UpstreamAccount


spec = importlib.util.spec_from_file_location(
    "pandora_endpoint",
    Path(__file__).resolve().parents[1] / "custom_components/pandora_cas/api.py",
)
api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)


class EndpointTests(unittest.IsolatedAsyncioTestCase):
    async def test_authentication_and_devices(self):
        for base_url in api.API_SERVERS:
            with self.subTest(base_url=base_url):
                await self.check_authentication_and_devices(base_url)

    async def check_authentication_and_devices(self, base_url):
        session = MagicMock()
        account = api.PandoraOnlineAccount(
            session=session, username="test", password="test", base_url=base_url
        )
        account._handle_dict_response = AsyncMock(
            side_effect=[{"access_token": "test-token"}, {"user_id": 123}]
        )
        account._handle_list_response = AsyncMock(return_value=[])

        await account.async_authenticate()
        await account.async_refresh_devices()

        self.assertEqual(
            [call.args[0] for call in session.post.call_args_list],
            [
                f"{base_url}/oauth/token",
                f"{base_url}/api/users/login",
            ],
        )
        self.assertEqual(
            session.get.call_args.args[0], f"{base_url}/api/devices"
        )
        self.assertEqual(account.user_id, 123)

    async def test_websocket_endpoint(self):
        for base_url in api.API_SERVERS:
            with self.subTest(base_url=base_url):
                await self.check_websocket_endpoint(base_url)

    async def check_websocket_endpoint(self, base_url):
        session = MagicMock()
        session.ws_connect.return_value.__aenter__.return_value.closed = True
        account = api.PandoraOnlineAccount(
            session=session, access_token="test-token", base_url=base_url
        )

        async for _ in account._iterate_websockets():
            self.fail("A closed websocket must not yield messages")

        self.assertEqual(
            session.ws_connect.call_args.args[0],
            f"{base_url}/api/v4/updates/ws?access_token=test-token",
        )

    def test_existing_accounts_default_to_new_server(self):
        account = api.PandoraOnlineAccount(session=MagicMock())
        self.assertEqual(account.BASE_URL, "https://pandora-on.com")

    def test_accounts_can_use_different_servers(self):
        legacy = api.PandoraOnlineAccount(
            session=MagicMock(), base_url="https://pro.p-on.ru"
        )
        new = api.PandoraOnlineAccount(session=MagicMock())
        self.assertEqual(legacy.BASE_URL, "https://pro.p-on.ru")
        self.assertEqual(new.BASE_URL, "https://pandora-on.com")

    def test_unsupported_server_is_rejected(self):
        with self.assertRaises(ValueError):
            api.PandoraOnlineAccount(
                session=MagicMock(), base_url="https://example.com"
            )

    def test_upstream_client_is_not_modified(self):
        self.assertEqual(UpstreamAccount.BASE_URL, "https://pro.p-on.ru")


if __name__ == "__main__":
    unittest.main()
