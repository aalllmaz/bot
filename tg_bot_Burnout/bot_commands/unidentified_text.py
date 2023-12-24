from aiogram import types
from loader import dp


@dp.message_handler()
async def unidentified_text(message: types.Message):
    await message.answer(f"Команда не распознана")