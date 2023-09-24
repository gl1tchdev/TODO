from telebot.async_telebot import AsyncTeleBot
from .handlers.register import register_user
from .handlers.buttons import handle_buttons


def setup_handlers(bot: AsyncTeleBot) -> AsyncTeleBot:
    bot.register_message_handler(register_user, commands=['start'], pass_bot=True)
    bot.register_callback_query_handler(handle_buttons, func=lambda callback: True, pass_bot=True)
    return bot
