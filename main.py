# i have some problems with english language :D

# import dependencies

import aiogram

from bot_modules.dispatcher import *
from bot_modules.bot_client import *
from bot_modules.donations import *

# ----------------------------------------------------- #

# start bot executing
if __name__ == '__main__':
	aiogram.executor.start_polling(dp, skip_updates = True) # start bot executing

