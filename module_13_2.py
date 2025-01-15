from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
api = "7314899914:AAHcsc1SyUJccc3bK3jNxYvAkCdAfC8fxas"
bot = Bot(token = api)
dp = Dispatcher()
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')
    print('Привет! Я бот, помогающий твоему здоровью.')
@dp.message()
async def all_massages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print('Введите команду /start, чтобы начать общение.')
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())

