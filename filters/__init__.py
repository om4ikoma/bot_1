from aiogram import Dispatcher

from .chat_subcribe import IsSubcriber

def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsSubcriber)