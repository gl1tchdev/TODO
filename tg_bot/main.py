from telebot.async_telebot import AsyncTeleBot
from telebot import TeleBot
from telebot.util import quick_markup
from . import handler
from TODO.settings import TELEGRAM_TOKEN


bot_instance = AsyncTeleBot(TELEGRAM_TOKEN)
async_bot_instance = handler.setup_handlers(bot_instance)
sync_bot_instance = TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')


def send_message(chat_id: int, text: str, task_id: int):
    keyboard = {'✅ Done!':
                    {
                        'callback_data': task_id
                     },
                '❌ Not yet':
                    {
                        'callback_data': 'pass'
                     }}
    markup = quick_markup(keyboard)
    return sync_bot_instance.send_message(chat_id=chat_id, text=text, reply_markup=markup)