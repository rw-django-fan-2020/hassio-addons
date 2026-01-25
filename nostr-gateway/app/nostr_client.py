from nostr_sdk import Keys, Client, Filter, EventKind, decrypt
import requests
import time
from pathlib import Path

KEY_PATH = Path("/data/nostr.key")

def load_or_create_keys():
    if KEY_PATH.exists():
        nsec = KEY_PATH.read_text().strip()
        keys = Keys.parse(nsec)
    else:
        keys = Keys.generate()
        KEY_PATH.write_text(keys.secret_key().to_bech32())
        KEY_PATH.chmod(0o600)
        print(f"[nostr] new key generated: npub={keys.public_key().to_bech32()}")
    return keys

class NostrClient:
    def __init__(self, relays, webhook, allowed_pubkeys):
        self.keys = load_or_create_keys()
        self.client = Client(self.keys)
        self.webhook = webhook
        self.allowed = set(allowed_pubkeys)

        for relay in relays:
            self.client.add_relay(relay)

        print(f"[nostr] npub={self.keys.public_key().to_bech32()}")

    def run(self):
        self.client.connect()

        flt = Filter().kind(EventKind.ENCRYPTED_DIRECT_MESSAGE)
        self.client.subscribe([flt], self.on_event)

        print("[nostr] listening for DMs...")
        while True:
            time.sleep(1)

    def on_event(self, event):
        sender = event.pub_key()

        if self.allowed and sender not in self.allowed:
            return

        try:
            content = decrypt(self.keys.secret_key(), sender, event.content())
        except Exception as e:
            print(f"[nostr] failed to decrypt DM from {sender}: {e}")
            return

        payload = {
            "pubkey": sender,
            "content": content,
            "event_id": event.id()
        }

        try:
            r = requests.post(self.webhook, json=payload, timeout=10)
            r.raise_for_status()
            reply = r.json().get("reply")
            if reply:
                self.send_dm(sender, reply)
        except Exception as e:
            print(f"[nostr] failed to send webhook or reply: {e}")

    def send_dm(self, pubkey, message):
        try:
            self.client.send_direct_msg(pubkey, message)
        except Exception as e:
            print(f"[nostr] failed to send DM to {pubkey}: {e}")
