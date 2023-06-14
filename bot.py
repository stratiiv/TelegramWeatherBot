import os
import telebot
from services import get_current_weather


BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    greeting = "Hello! This is Weather Bot. To get current weather in your "\
               "place, please use /weather command."
    bot.reply_to(message, greeting)


@bot.message_handler(commands=['weather'])
def weather_handler(message):
    text = "What's your location? (type in your city "\
           "or share your current location with the bot.)"
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, location_handler)


@bot.message_handler(content_types=['location'])
def location_handler(message):
    if message.location:
        location = (message.location.latitude, message.location.longitude)
    else:
        location = message.text
    try:
        temp, description = get_current_weather(location)
        text = f"Currently it is {temp}°C, {description} in {location}"
        bot.send_message(message.chat.id, text)
    except Exception as e:
        error_message = "Sorry, an error occurred while fetching the weather data. "\
                        "Please make sure you have entered the correct location."

        bot.send_message(message.chat.id, error_message)
        print(f"Error fetching weather data: {e}")


@bot.message_handler()
def default_handler(message):
    error_message = "Sorry, I'm currently unable to process this command. "\
                    "Please try again later."

    bot.reply_to(message, error_message)


bot.infinity_polling()