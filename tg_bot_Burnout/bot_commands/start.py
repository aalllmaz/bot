from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\nЭто бот был создан в качестве экзаменационной "
                         "работы\nНапишите команду /help чтобы получить подробную информацию о его возможностях")
