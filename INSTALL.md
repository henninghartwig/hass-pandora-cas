# Switching to pandora-on.com

This change replaces the unreachable domain `pro.p-on.ru` with
`https://pandora-on.com` for authentication, the HTTP API, and WebSockets.
Translations are also loaded from the new domain. The installed Python library
is not modified.

## Installation

1. Back up the existing `/config/custom_components/pandora_cas` directory.
2. Copy the entire `custom_components/pandora_cas` directory from this repository
   to `/config/custom_components/pandora_cas`.
3. Restart Home Assistant.

You do not need to delete the existing integration. Your username and password
are retained. The modified integration will send them to `pandora-on.com`.
A later HACS update may overwrite this local change.

## Validation

The public endpoints `/api/devices` and `/oauth/token` return JSON errors when
called without authentication; `/local/web/en.json` returns a translation object.
An OAuth test using the built-in client credentials from `pandora-cas==0.0.16`
on November 2, 2026 returned HTTP 200 and an access token. The first connection
attempt failed; the second succeeded. Full authentication with personal
credentials and the WebSocket connection have not yet been tested with a real
account.

Offline tests using the library pinned in the manifest, `pandora-cas==0.0.16`:

```sh
python -m unittest discover -s tests -v
```
