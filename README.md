## This is a very simple telegram bot for sending donations. Only Qiwi donations are available (could not test on other wallets)

### Installation and run:
`pip install -r requirements.txt`

`python3 main.py` or just `main.py` (On Windows)

# ------------------------ 

The `main.py` module the main module you need to run.

In the `\bot_modules\data\bot_configs.py` module, you need to register the bot's telegram token and the public Qiwi P2P token.

In the `\bot_modules\message_data\messages.py` module, you can change the messages that the bot will send to the user.

In the `\bot_modules\message_data\inline_buttons.py` module, you can change inline telegram buttons or add new ones.

# ------------------------ 

The `bot_client.py` module is the main module that handles commands sent to the user.
