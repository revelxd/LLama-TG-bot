# Very simple Telegram AI Bot with Llama

This bot uses the Llama model via the OpenRouter API to generate responses to user messages in Telegram. I wrote it in 15 minutes, just for fun.

## Setup

1. Create a bot in Telegram via [@BotFather](https://t.me/BotFather) and obtain the bot token.
2. Get an API key from [OpenRouter](https://openrouter.ai/settings/keys).
3. Open the `main.py` file and fill in the following variables:
   ```python
   BOT_TOKEN = "your_bot_token"
   OPENROUTER_API_KEY = "your_openrouter_key"
   ```

## Installation

1. Ensure you have Python 3.7 or higher installed.
2. Install the required dependencies:
   ```bash
   pip install pyTelegramBotAPI requests
   ```

## Running the Bot

1. Start the bot with the command:
   ```bash
   python main.py
   ```
   Or use any other convenient method.
2. After launching, you will see the message "Бот запущен..."

## Usage

1. Find your bot in Telegram by the @username you specified during creation.
2. Send the `/start` command to begin.
3. Simply send any message to the bot, and it will respond using the Llama model.

## Features

- The bot uses the `meta-llama/llama-4-scout:free` model.
- Supports all types of text messages.
- Automatically handles API errors.
- Uses a free model (no need to pay for further subscription extensions—it's free forever).

## Notes

- The bot only works with text messages.
- The bot may not support certain Markdown formatting.
- Response speed depends on the load of the OpenRouter API.
