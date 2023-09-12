from telebot.async_telebot import AsyncTeleBot
from . import handler
from TODO.settings import TELEGRAM_TOKEN


bot_instance = AsyncTeleBot(TELEGRAM_TOKEN)
bot = handler.setup_handlers(bot_instance)


