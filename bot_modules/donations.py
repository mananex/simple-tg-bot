# import dependencies

import aiogram
import requests

from bot_modules.dispatcher import bot, dp
from bot_modules.data import bot_configs

@dp.callback_query_handler(text = ['commands_donate_callback'])
async def donate_handler(call: aiogram.types.CallbackQuery):
	await call.answer('Донат')
	donate_markup = aiogram.types.InlineKeyboardMarkup(resize_keyboard = True)
	donate_markup.add(aiogram.types.InlineKeyboardButton(text = 'Donate', url = f'https://oplata.qiwi.com/create?publicKey={bot_configs.QIWI_P2P_PUBLIC_KEY}&amount=100'))

	await call.message.answer('<b>Donate link:</b>', parse_mode = 'html', reply_markup = donate_markup)

