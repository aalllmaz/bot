from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Список всех команд"),
            types.BotCommand("on_start_test", "Выбрать опрос для прохождения"),
        ]
    )
