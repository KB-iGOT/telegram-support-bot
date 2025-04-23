# KB Telegram Support Bot

The Telegram Bot is a Python-based bot that interacts with the KB Agent API Server via Telegram. It allows users to perform various actions and access information from the API Server through the convenience of a Telegram chat interface.

## Prerequisites

- Python 3.12+
- Starlette
- Redis (for user session)
- python-telegram-bot library
- Telegram bot token
- Tunnel - Tunneling exposes your local system to the services on the web by tunneling the external calls to your local system. Either of these two popular services can be used:
   - Loophole - Please refer to the [Loophole Quickstart Guide](https://loophole.cloud/download/) for installation.
   - Ngrok - Please refer to the [Ngrok Quickstart Guide](https://ngrok.com/docs#getting-started) for installation.
- Virtual environment (recommended).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KB-iGOT/telegram_support_bot.git
   cd telegram_support_bot
   ```
2. **Install Dependencies**

   ```bash
   pip install uv && uv sync
   ```

3.  **Active a virtual environment:**

    ```bashs
    source .venv/bin/activate  # On Linux/macOS
    source .venv\Scripts\activate  # On Windows
    ```


4. **Set up your Telegram bot:**
   - Create a new bot on Telegram and obtain the [bot token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).
   - Set up a webhook URL (using a public domain with [SSL/TLS support](https://core.telegram.org/bots/webhooks#always-ssl-tls))

     If you're having any trouble setting up webhooks, please check out this [amazing guide to webhooks](https://core.telegram.org/bots/webhooks).

5. **Set up environment variables:**
   - Create a .env file in the project root and add the following variables:
   ```bash
   LOG_LEVEL="INFO" # INFO, DEBUG, ERROR

   TELEGRAM_BASE_URL=https://your-telegram-callback-url.com
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   TELEGRAM_BOT_NAME=your-telegram-bot-name
   
   KB_AGENT_BASE_URL=https://your-activity-api-url.com 
   SUPPORTED_LANGUAGES=en,bn,gu,hi,kn,ml,mr,or,pa,ta,te
   
   REDIS_HOST=your-redis-host
   REDIS_PORT=your-redis-port
   REDIS_INDEX=your-redis-index
   ```
   **Note:** This telegram bot only supports the following languages: en, bn, gu, hi, kn, ml, mr, or, pa, ta, te.

   You can find further configuration parameters in `src/core/config.py`.

## Usage

1. Ensure Redis is running. If not installed, you can download it from [official Redis website](https://redis.io/).

2. Start the Starlette app:
   ```bash
   python3 telegram_webhook.py
   ```

3. Once the Telegram bot is up and running, you can interact with it through your Telegram chat app. Start a chat with the bot and use the available commands and features to perform actions and retrieve information from the API Server.

   - The bot provides the following commands:

      ```bash 
      /start: Start the conversation with the bot
      ```
   - Select preferred language
   - Start querying questions

## Configuration (config.ini)

| Variable                        | Description                                                                                    | Default Value                        |
|:--------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------|
| default.language      | This configuration sets the default language for the chatbot interaction. When a user starts a conversation, the chatbot will use this language unless explicitly changed. | en                                    |
| default.welcome_msg         | This configuration defines the initial message displayed by the chatbot when a user starts a conversation.      | Namaste 🙏 Welcome to *iGOT Assisstant* _(Powered by Bhashini)_                                |
| default.languages    | This configuration specifies the list of languages displayed by the chatbot  when a user starts a conversation.                                                           |  For example: [{"text": "English", "code": "en","index": 1}...{}]    |

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
