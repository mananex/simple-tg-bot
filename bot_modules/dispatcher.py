# import dependencies

import aiogram
from bot_modules.data import bot_configs

# ----- IMPORTANT VARIABLES ----- #

bot	= aiogram.Bot(bot_configs.TELE_API_TOKEN) 	# initialize telegram bot
dp	= aiogram.Dispatcher(bot)					# initialize telegram bot dispatcher

# ----- --------- --------- ----- #
