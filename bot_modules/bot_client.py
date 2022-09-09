# import dependencies

import aiogram

from bot_modules.dispatcher import dp, bot
from bot_modules.message_data import messages, inline_buttons

# ---------------- ---------- -------- ---------- ---------------- #

# on /start
@dp.message_handler(commands = ['start', 'help'])
async def start_info(message: aiogram.types.Message):
	await message.answer(messages.start_info, parse_mode = 'html') # send message to user

# on /commands
@dp.message_handler(commands = ['commands'])
async def commands(message: aiogram.types.Message):
	await message.answer(messages.commands_info, parse_mode = 'html', reply_markup = inline_buttons.commands_markup) # send message to user