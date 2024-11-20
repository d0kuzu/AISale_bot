import argparse
import asyncio
import logging

import coloredlogs
from aiogram import Bot, Dispatcher

from config import Environ
from services.telegram.register import TgRegister


async def start(environment: Environ):
    bot = Bot(token=environment.bot_token)
    dp = Dispatcher()

    tg_register = TgRegister(dp)
    tg_register.register()
    await dp.start_polling(bot)


if __name__ == "__main__":
    env = Environ()
    logging.basicConfig()
    coloredlogs.install()
    asyncio.run(start(env))