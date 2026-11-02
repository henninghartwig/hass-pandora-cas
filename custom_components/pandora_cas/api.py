"""Pandora API client using the reachable Pandora Online domain."""

from pandora_cas.account import PandoraOnlineAccount as _PandoraOnlineAccount

API_BASE_URL = "https://pandora-on.com"


class PandoraOnlineAccount(_PandoraOnlineAccount):
    """Use the same host for authentication, HTTP requests and WebSockets."""

    BASE_URL = API_BASE_URL
