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
        session = MagicMock()
        account = api.PandoraOnlineAccount(
            session=session, username="test", password="test"
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
                "https://pandora-on.com/oauth/token",
                "https://pandora-on.com/api/users/login",
            ],
        )
        self.assertEqual(
            session.get.call_args.args[0], "https://pandora-on.com/api/devices"
        )
        self.assertEqual(account.user_id, 123)

    async def test_websocket_endpoint(self):
        session = MagicMock()
        session.ws_connect.return_value.__aenter__.return_value.closed = True
        account = api.PandoraOnlineAccount(session=session, access_token="test-token")

        async for _ in account._iterate_websockets():
            self.fail("A closed websocket must not yield messages")

        self.assertEqual(
            session.ws_connect.call_args.args[0],
            "https://pandora-on.com/api/v4/updates/ws?access_token=test-token",
        )

    def test_upstream_client_is_not_modified(self):
        self.assertEqual(UpstreamAccount.BASE_URL, "https://pro.p-on.ru")


if __name__ == "__main__":
    unittest.main()
