# Changelog

## 0.1.0 (2026-01-25)
- Initial release
- Minimal Nostr DM Gateway Add-on
- Features:
  - Persistent Nostr identity (`nsec` stored in `/data/nostr.key`)
  - Connects to multiple relays
  - Receives encrypted direct messages (`kind:4`)
  - Forwards messages to a configurable webhook (n8n)
  - Sends webhook replies back as Nostr DMs
  - Optional PubKey whitelist
- Docker-based, works on amd64 and aarch64
- No conversation memory or AI included (handled externally)
