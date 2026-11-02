# Umstellung auf pandora-on.com

Diese Änderung ersetzt die nicht erreichbare Domain `pro.p-on.ru` durch
`https://pandora-on.com`. Sie gilt für die Anmeldung, HTTP-API und WebSockets.
Auch Übersetzungen werden von der neuen Domain geladen. Die installierte
Python-Bibliothek wird nicht verändert.

## Installation

1. Den vorhandenen Ordner `/config/custom_components/pandora_cas` sichern.
2. Den Ordner `custom_components/pandora_cas` aus diesem Repository vollständig
   nach `/config/custom_components/pandora_cas` kopieren.
3. Home Assistant neu starten.

Die vorhandene Integration muss nicht gelöscht werden. Benutzername und Passwort
bleiben erhalten. Die geänderte Integration sendet sie künftig an
`pandora-on.com`. Ein späteres HACS-Update kann die lokale Änderung überschreiben.

## Validierung

Die öffentlichen Endpunkte `/api/devices` und `/oauth/token` antworten mit
JSON-Fehlern für fehlende Authentifizierung; `/local/web/en.json` liefert ein
Übersetzungsobjekt. Ein OAuth-Test mit der eingebauten Client-Kennung von
`pandora-cas==0.0.16` am 02.11.2026 lieferte HTTP 200 und einen Access-Token.
Der erste Verbindungsversuch scheiterte; der zweite war erfolgreich.
Die vollständige Anmeldung mit persönlichen Zugangsdaten und die
WebSocket-Verbindung sind noch nicht am echten Konto getestet.

Offline-Tests mit der im Manifest festgelegten Bibliothek `pandora-cas==0.0.16`:

```sh
python -m unittest discover -s tests -v
```
