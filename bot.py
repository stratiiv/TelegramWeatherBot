import os
import telebot
from services import get_current_weather
from messages import get_message


BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    """Send a welcome message to the user."""
    greeting = get_message('greeting')
    bot.reply_to(message, greeting)


@bot.message_handler(commands=['weather'])
def weather_handler(message):
    """
    Handle the '/weather' command and prompt the user for their location.
    """
    text = get_message('weather_hint')
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, location_handler)


@bot.message_handler(content_types=['location'])
def location_handler(message):
    """
    Handle the user's location information and retrieve the weather data.
    """
    try:
        if message.location:
            location = (message.location.latitude, message.location.longitude)
            temp, description = get_current_weather(location)
            reply = get_message('weather_in_location').format(temp,
                                                              description)
        else:
            city = message.text
            temp, description = get_current_weather(city)
            reply = get_message('weather_in_city').format(temp, description,
                                                          city)
    except Exception as e:
        error_message = get_message('weather_fail')
        bot.send_message(message.chat.id, error_message)
        print(f"Error fetching weather data: {e}")
    else:
        bot.send_message(message.chat.id, reply)


@bot.message_handler()
def default_handler(message):
    """
    Handle all other messages that are not recognized as commands.
    """
    error_message = get_message('general_fail')
    bot.reply_to(message, error_message)


bot.infinity_polling()
