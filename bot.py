import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    greeting = "Hello! This is Weather Bot. To get started, simply type in "\
                "your location or share your current location with the bot."
    bot.reply_to(message, greeting)


bot.infinity_polling()