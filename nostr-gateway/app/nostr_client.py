from nostr_sdk import (
    Client,
    Keys,
    Filter,
    EventKind,
    decrypt
)
import requests
import time

class NostrClient:
    def __init__(self, relays, webhook, allowed_pubkeys):
        self.keys = Keys.generate()  # 🔴 später persistent machen!
        self.client = Client(self.keys)
        self.webhook = webhook
        self.allowed = set(allowed_pubkeys)

        for relay in relays:
            self.client.add_relay(relay)

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

        content = decrypt(
            self.keys.secret_key(),
            sender,
            event.content()
        )

        payload = {
            "pubkey": sender,
            "content": content,
            "event_id": event.id()
        }

        r = requests.post(self.webhook, json=payload, timeout=10)
        r.raise_for_status()

        reply = r.json().get("reply")
        if reply:
            self.send_dm(sender, reply)

    def send_dm(self, pubkey, message):
        self.client.send_direct_msg(pubkey, message)
