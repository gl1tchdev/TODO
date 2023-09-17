from telebot.async_telebot import AsyncTeleBot
from telebot import TeleBot
from . import handler
from TODO.settings import TELEGRAM_TOKEN


bot_instance = AsyncTeleBot(TELEGRAM_TOKEN)
async_bot_instance = handler.setup_handlers(bot_instance)
sync_bot_instance = TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')


def send_message(chat_id: int, text: str):
    sync_bot_instance.send_message(chat_id=chat_id, text=text)