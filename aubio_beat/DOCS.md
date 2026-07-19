# Snapcast Server – Home Assistant Add-on

---

## 🇬🇧 English

This add-on provides a **Snapcast Server** for Home Assistant OS / Supervised. Snapcast enables **synchronized audio playback** across multiple clients (e.g. Snapclient, Mopidy, Librespot, custom FIFO or TCP streams).

---

### 📦 Add-on Information

* **Name:** snapcast-server
* **Version:** `0.34.0-r0`
* **Slug:** `snapcastserver`
* **Ingress:** enabled
* **Panel Icon:** `mdi:music-box-outline`
* **Project URL:**
  [https://github.com/rw-django-fan-2020/hassio-addons/tree/main/snapcastserver](https://github.com/rw-django-fan-2020/hassio-addons/tree/main/snapcastserver)

---

### 🚀 Features

* Full Snapcast Server
* Pipe, TCP and broadcast stream support
* HTTP & TCP JSON-RPC APIs
* Ingress web interface
* Access to `/share` (e.g. FIFOs)
* Ideal for Mopidy, Librespot, FFmpeg and custom audio sources

---

### 🔧 Default Configuration (`options`)

```yaml
use_custom_config: false
stream:
  sources:
    - pipe:///share/snapfifo/snapfifo?name=default
    - pipe:///share/snapfifo/librespot?name=SpotifyConnect&sampleformat=44100:16:2
    - pipe:///share/snapfifo/mopidy?name=Mopidy&sampleformat=44100:16:2
    - tcp://0.0.0.0?port=4953&name=snapbroadcast
  buffer: 1000
  codec: flac
  send_to_muted: 'false'
  sampleformat: '48000:16:2'
http:
  enabled: 'true'
  doc_root: " "
tcp:
  enabled: 'true'
logging:
  enabled: 'true'
server:
  threads: "-1"
  datadir: "/share/snapcast/"
```

---

### 🧠 Option Details

#### `use_custom_config`

* **false**: Configuration is generated from add-on options (default)
* **true**: Use a custom `snapserver.conf` (e.g. from `/share`)

---

### 🎵 Stream Configuration (`stream`)

#### `sources`

Defines the available audio streams.

Examples:

* **FIFO / Pipe:**

  ```text
  pipe:///share/snapfifo/snapfifo?name=default
  ```

* **Librespot:**

  ```text
  pipe:///share/snapfifo/librespot?name=SpotifyConnect&sampleformat=44100:16:2
  ```

* **Mopidy:**

  ```text
  pipe:///share/snapfifo/mopidy?name=Mopidy&sampleformat=44100:16:2
  ```

* **TCP Broadcast:**

  ```text
  tcp://0.0.0.0?port=4953&name=snapbroadcast
  ```

⚠️ FIFOs must be created and written to by external services.

---

#### Other Stream Options

* **buffer**: Buffer size in milliseconds
* **codec**: Audio codec (recommended: `flac`)
* **sampleformat**: `samplerate:bits:channels`
* **send_to_muted**: Keep muted clients synchronized

---

### 🌐 HTTP Configuration

Enables the HTTP JSON-RPC API and ingress UI.

---

### 🔌 TCP Configuration

Enables the TCP JSON-RPC API (used by snapclient).

---

### 🧵 Server Settings

* **threads**: `-1` = automatic
* **datadir**: persistent Snapcast data directory

---

### 🔌 Ports

| Port     | Description             |
| -------- | ----------------------- |
| 1704/tcp | Audio stream            |
| 1705/tcp | TCP JSON-RPC            |
| 1780/tcp | HTTP JSON-RPC / Ingress |
| 4953/tcp | TCP broadcast stream    |

---

### 🧩 Supported Architectures

`armhf`, `armv7`, `aarch64`, `amd64`, `i386`

---

### 🛠️ Best Practices

* Create FIFOs under `/share`
* Use identical sample formats for all sources
* Increase buffer if dropouts occur

---

## 🇩🇪 Deutsch

Dieses Add-on stellt einen **Snapcast Server** für Home Assistant OS / Supervised bereit. Snapcast ermöglicht die **synchrone Audiowiedergabe** über mehrere Clients (z. B. Snapclient, Mopidy, Librespot oder eigene Audioquellen).

---

### 📦 Add-on Informationen

* **Name:** snapcast-server
* **Version:** `0.34.0-r0`
* **Slug:** `snapcastserver`
* **Ingress:** aktiviert
* **Panel Icon:** `mdi:music-box-outline`
* **Projekt-URL:**
  [https://github.com/rw-django-fan-2020/hassio-addons/tree/main/snapcastserver](https://github.com/rw-django-fan-2020/hassio-addons/tree/main/snapcastserver)

---

### 🚀 Funktionen

* Vollwertiger Snapcast Server
* Pipe-, TCP- und Broadcast-Streams
* HTTP- & TCP-JSON-RPC APIs
* Ingress-Weboberfläche
* Zugriff auf `/share` (z. B. FIFOs)
* Ideal für Mopidy, Librespot, FFmpeg

---

### 🧠 Wichtige Hinweise

* FIFOs müssen extern erstellt werden
* Einheitliche Sampleformate empfohlen
* Bei Audioaussetzern `buffer` erhöhen
* Für maximale Kontrolle: `use_custom_config: true`

---

### 📚 Further Reading / Weiterführende Links

* Snapcast: [https://github.com/badaix/snapcast](https://github.com/badaix/snapcast)
* Snapserver Configuration: [https://github.com/badaix/snapcast/blob/develop/doc/configuration.md](https://github.com/badaix/snapcast/blob/develop/doc/configuration.md)

---

🎶 Enjoy synchronized audio / Viel Spaß mit synchronem Audio
