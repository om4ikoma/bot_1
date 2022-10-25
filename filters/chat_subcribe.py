from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data import config
from loader import bot, dp


class IsSubcriber(BoundFilter):
    async def check(self, message: types.Message):
        subscribed = 0
        for chat_id in config.chat_id:
            sub = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
            if sub.status != types.ChatMemberStatus.LEFT:
                subscribed += 1
            else:
                break
        else:
            if subscribed == len(config.chat_id):
                return True

        markup = InlineKeyboardMarkup(row_width=1,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Телеграмм чат:',
                                                                   url='https://t.me/+fZFv6dfmHPE3YmUy')
                                          ]
                                      ])
        await dp.bot.send_message(chat_id=message.from_user.id,
                                  text='Подпишитесь на телеграмм чат и повторите попытку',
                                  reply_markup=markup)
