# Nostr Gateway Add-on for Home Assistant

**Version:** 0.1.0  
**Maintainer:** rw-django-fan-2020

---

## Description

This Home Assistant Add-on acts as a **Nostr DM Gateway**.  
It receives encrypted direct messages (DMs) and forwards them to a configurable **n8n webhook** for processing (e.g., AI conversation). Replies from the webhook are sent back to the sender as encrypted Nostr DMs.

> **Note:** This Add-on does NOT handle AI or conversation memory. That should be handled externally (e.g., n8n or other backend).

---

## Features

- Persistent Nostr identity (`nsec` stored in `/data/nostr.key`)
- Connects to multiple relays
- Receives encrypted direct messages (`kind:4`)
- Forwards messages to webhook (n8n)
- Sends webhook replies back as Nostr DMs
- Optional PubKey whitelist for access control
- Runs as a stable HA Add-on (amd64 & aarch64)

---

## Configuration

### Options

```yaml
relays:
  - wss://relay.damus.io
  - wss://nostr.wine
n8n_webhook: http://n8n:5678/webhook/nostr-ai
allowed_pubkeys:
  - npub1abcdef...
