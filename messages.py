MESSAGES = {
    'weather_hint': "What's your location? (type in your city "
                    "or share your current location with the bot.)",

    'weather_fail': "Sorry, an error occurred while fetching the weather data."
                    " Please make sure you have entered the correct location.",

    'general_fail': "Sorry, I'm currently unable to process this command. "
                    "Please try again later.",

    'weather_in_city': "Currently it is {:.1f}°C, {} in {}",

    'weather_in_location': "Currently it is {:.1f}°C, {} in your location",

    'greeting': "Hello! This is Weather Bot. To get current weather in your "
                "place, please use /weather command."
}


def get_message(message_key: str) -> str:
    return MESSAGES[message_key]