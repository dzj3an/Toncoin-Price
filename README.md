# Toncoin Price Bot

This Telegram bot posts the price of **Toncoin** on a specific channel every minute. It is useful for those who want to closely follow Toncoin quote.

Support the creator by joining their development channel on Telegram: [J3an | Dev](https://t.me/j3d3v)

## 💖 Support the Developer

If you found this tool useful, consider supporting the developer by making a donation. Your support helps maintain and improve this project.

☕️ Donate here: [dzj3an.github.io/donate.html](https://dzj3an.github.io/donate.html)

## Features

- Get the price of Toncoin from an official API.
- Send updates to the configured Telegram channel.
- You can turn off the process or turn it on whenever you like.


You can see the functionalities of the Bot by joining the following channel:  
[https://t.me/iTonPrice](https://t.me/iTonPrice)

---

## Requirements

Make sure you have the following dependencies installed:

- [**kurigram**](https://pypi.org/project/kurigram/)
- [**pyromod**](https://pypi.org/project/pyromod/)
- [**TgCrypto**](https://pypi.org/project/TgCrypto/)
- [**pytonapi**](https://pypi.org/project/pytonapi/)

You can install them by running:

```bash
pip install -r requirements.txt
```

---

## Configuration

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dzj3an/Toncoin-Price.git
   cd Toncoin-Price
   ```

2. **Get your credentials:**

   - **BOT_TOKEN**: Generate a token for your bot from [@ BotFather](https://t.me/BotFather) on Telegram.
   - **API_HASH** y **API_ID**: Create an application on the site of [Telegram](https://my.telegram.org/auth) to get these credentials.
   - **TON_TOKEN**: Sign up for [Ton Console](https://tonconsole.com/) to get an access token.

3. **Configure credentials in `config.py`:**

   ```python
   BOT_TOKEN = "YOUR_BOT_TOKEN"
   API_HASH = "YOUR_API_HASH"
   API_ID = YOUR_API_ID  # Example: 12345678
   TON_TOKEN = "YOUR_TON_TOKEN"
   OWNERS_ID = [123456789]  # Bot administrators IDs
   CHANNEL_TON = -1001234567890  # Channel ID where prices will be sent
   ```

---

## Execution

Run the bot with the following command:

```bash
python main.py
```

When you start, go to the Bot and press /menu then turn on the process and you're done.

---


## Credits

This bot was created by [J3an](https://github.com/dzj3an).


You would help a lot if you follow the page of the bookstore that we use in this bot to connect with Telegram. This library is **kurigram**, a fork of **pyrogram**.  

Find information on your official channel:  
[Kurigram](https://t.me/kurigram_news)

Leave your star in this repository and share it with your friends. 😊
