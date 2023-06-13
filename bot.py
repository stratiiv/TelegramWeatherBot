import os
import telebot
from services import get_current_weather


BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    greeting = "Hello! This is Weather Bot. To get started, simply type in "\
                "your location or share your current location with the bot."
    bot.reply_to(message, greeting)


@bot.message_handler(commands=['weather'])
def weather_handler(message):
    text = "What's your location?"
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, location_handler)


def location_handler(message):
    location = message.text
    temp, description = get_current_weather(location)
    text = f"Currently it is {temp}°C, {description} in {location}"
    bot.send_message(message.chat.id, text)


bot.infinity_polling()