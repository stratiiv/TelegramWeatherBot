# Telegram Weather Bot

This is a Telegram bot that provides weather information based on user input. The bot can retrieve the current weather conditions for a specific city or the user's current location.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install `pipenv` if you haven't already:
```bash
pip install pipenv
```
4. Install the project dependencies using pipenv:
```bash
pipenv install
```

5. Obtain an API token for the OpenWeatherMap API:

   * Go to the OpenWeatherMap website and sign up for an account.
   * Retrieve your API key.
6. Go to [@BotFather](https://telegram.me/botfather) on Telegram and create a new bot. Follow the instructions provided by BotFather to create your bot and obtain the API token.

7. Set up environment variables:
   * Create a new file named `.env` in the project's root directory.

   * Replace `YOUR_BOT_TOKEN` and `YOUR_API_KEY` with your values:
     ```
     BOT_TOKEN=YOUR_BOT_TOKEN
     API_KEY=YOUR_API_KEY
     ```
8. Launch the virtual environment:
```bash
pipenv shell
```
9. Start the bot:

```shell
python bot.py
```
## Usage
* Send a `/start` or `/hello` command to receive a welcome message from the bot.
* Use the `/weather` command to request weather information.
* If prompted for a location, you can provide a city name or share your current location.
* The bot will respond with the current temperature and weather description for the specified location.
## Contributing
Contributions to the Telegram Weather Bot are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
## License

[MIT](https://choosealicense.com/licenses/mit/)