import telebot
import requests
import json

# конфигурация
BOT_TOKEN = ""
OPENROUTER_API_KEY = ""
MODEL = "meta-llama/llama-4-scout:free"

# инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

def get_ai_response(message):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": message}]
    }
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"An error occurred while accessing the API: {str(e)}"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Hi! I'm a fast AI Llama bot. Just send me a message and I'll reply you with a response."
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # отправляем "печатает..." статус
    bot.send_chat_action(message.chat.id, 'typing')
    
    # получаем ответ от AI
    ai_response = get_ai_response(message.text)
    
    # отправляем ответ пользователю
    bot.reply_to(message, ai_response, parse_mode='Markdown')

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
