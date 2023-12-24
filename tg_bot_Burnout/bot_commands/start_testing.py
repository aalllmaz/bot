from aiogram.dispatcher.filters import Command
from loader import dp
from aiogram import types


@dp.message_handler(Command("on_start_test"))
async def on_start_test(message: types.Message):
        await message.answer("Какой тест хотите пройти? \nУровень профессионального самовыгорания "
                             "/on_start_burnout_test \nТип личности /on_start_personality_test")
