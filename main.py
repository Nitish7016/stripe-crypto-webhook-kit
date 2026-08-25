import os
import hmac
import hashlib
import time
import json
import urllib.request
from typing import Dict, Any

def verify_stripe_signature(payload_bytes: bytes, sig_header: str, secret: str, tolerance: int = 300) -> bool:
    try:
        pairs = dict(item.split("=", 1) for item in sig_header.split(","))
        timestamp = pairs.get("t")
        expected_sig = pairs.get("v1")
        if not timestamp or not expected_sig:
            return False
        if abs(time.time() - int(timestamp)) > tolerance:
            return False
        signed_payload = f"{timestamp}.".encode("utf-8") + payload_bytes
        computed = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
        return hmac.compare_digest(computed, expected_sig)
    except Exception:
        return False

def dispatch_discord(webhook_url: str, title: str, description: str, color: int = 0x2ea043):
    payload = {
        "embeds": [{
            "title": title,
            "description": description,
            "color": color,
            "footer": {"text": "⚡ Nitish Webhook Dispatcher"}
        }]
    }
    req = urllib.request.Request(webhook_url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return resp.status

def dispatch_telegram(bot_token: str, chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return resp.status

if __name__ == "__main__":
    print("[+] Stripe & Crypto Webhook Dispatcher Engine Ready.")
