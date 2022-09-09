# import dependencies
import aiogram

# ----------------------------------------------------------#

# inline markup on /commands #

commands_markup = aiogram.types.InlineKeyboardMarkup(resize_keyboard = True) # initialize inline keyboard markup 
commands_markup.add(aiogram.types.InlineKeyboardButton(text = '➕', callback_data = 'commands_donate_callback')) # add buttons to keyboard

# ------ ------ -- --------- #

# ----------------------------------------------------------#
