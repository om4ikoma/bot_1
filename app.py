from aiogram.utils import executor

async def on_startup(dp):
    print('Бот запущен')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
