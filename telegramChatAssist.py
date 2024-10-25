import requests
from telegram.ext import Updater, MessageHandler, Filters

import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
HF_SPACE_API_URL = os.getenv('HF_SPACE_API_URL')

# Define a message handler function
def handle_message(update, context):
    user_message = update.message.text
    chat_id = update.message.chat_id
    
    # Forward the user's message to the Hugging Face Space API
    response = requests.post(HF_SPACE_API_URL, json={"input": user_message})
    ai_reply = response.json().get("data", ["Error generating response."])[0]
    
    # Send the model's reply to the user
    context.bot.send_message(chat_id=chat_id, text=ai_reply)

# Set up the bot
updater = Updater(TELEGRAM_TOKEN)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
updater.idle()
