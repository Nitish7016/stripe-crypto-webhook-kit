# ⚡ Stripe & Crypto Webhook Multi-Channel Dispatcher Kit

Production-ready, lightweight webhook dispatcher that captures raw events from **Stripe**, **Lemon Squeezy**, and **Solana Pay**, verifies HMAC cryptographic signatures, and dispatches instant notifications to **Discord**, **Telegram**, and **Slack**.

---

## 🚀 Features

- 🔒 **Cryptographic Signature Verification**: Built-in HMAC-SHA256 verification for Stripe and LemonSqueezy to reject forged payloads.
- 🪙 **Crypto & Web3 Native**: Supports Solana Pay and Alchemy transaction webhooks.
- 📢 **Multi-Channel Dispatching**: Formatted embeds for Discord Webhooks, Telegram Bots (`sendMessage`), and Slack incoming webhooks.
- ⚡ **Zero-Config Serverless**: Deploy in 1 click to Vercel, AWS Lambda, Cloudflare Workers, or run as a standalone FastAPI server.
- 🛡️ **Failure Retry & Idempotency**: Deduplicates event IDs to prevent duplicate alert spam.

---

## 📦 Quickstart

### 1. Clone & Install
```bash
git clone https://github.com/Nitish7016/stripe-crypto-webhook-kit.git
cd stripe-crypto-webhook-kit
pip install -r requirements.txt
```

### 2. Configure `.env`
```env
STRIPE_WEBHOOK_SECRET=whsec_your_secret_here
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
TELEGRAM_CHAT_ID=123456789
```

### 3. Run Locally
```bash
python main.py
```

---

## 📄 License
MIT License. Created by Nitish Developer Suite.
