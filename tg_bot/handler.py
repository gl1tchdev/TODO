from telebot.async_telebot import AsyncTeleBot
from .handlers.register import register_user


def setup_handlers(bot: AsyncTeleBot) -> AsyncTeleBot:
    bot.register_message_handler(register_user, commands=['start'], pass_bot=True)
    return bot
