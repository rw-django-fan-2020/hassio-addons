import yaml
from nostr_client import NostrClient

CONFIG_PATH = "/data/options.yaml"

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

client = NostrClient(
    relays=config["relays"],
    webhook=config["n8n_webhook"],
    allowed_pubkeys=config.get("allowed_pubkeys", [])
)

client.run()
