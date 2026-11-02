"""Pandora API client with a server selected per account."""

from pandora_cas.account import PandoraOnlineAccount as _PandoraOnlineAccount

API_BASE_URL = "https://pandora-on.com"
CONF_API_URL = "api_url"
API_SERVERS = {
    API_BASE_URL: "pandora-on.com (new)",
    "https://pro.p-on.ru": "pro.p-on.ru (legacy)",
}


class PandoraOnlineAccount(_PandoraOnlineAccount):
    """Use the same host for authentication, HTTP requests and WebSockets."""

    BASE_URL = API_BASE_URL

    def __init__(self, *args, base_url: str = API_BASE_URL, **kwargs):
        if base_url not in API_SERVERS:
            raise ValueError("Unsupported Pandora API server")
        super().__init__(*args, **kwargs)
        self.BASE_URL = base_url
