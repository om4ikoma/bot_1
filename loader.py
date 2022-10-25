from aiogram import Bot, Dispatcher, types
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)


dp = Dispatcher(bot)

if __name__ == "main":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(skip_updates=True)