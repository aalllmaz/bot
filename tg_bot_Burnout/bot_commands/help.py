from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Запустить бота",
            "/help - Получить список команд",
            "/about - Получить аннотацию к проекту",
            "/on_start_test - Выбрать тест")

    await message.answer("\n".join(text))
