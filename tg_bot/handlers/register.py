import telebot.types
from telebot.async_telebot import AsyncTeleBot
from telebot.util import extract_arguments
from accounts.models import Telegram
from TODO.settings import HOST_NAME
from threading import Thread


def write_id(message: telebot.types.Message, user_id_str):
    tg = Telegram.objects.get(tg_random_salt=user_id_str)
    tg.tg_chat_id = message.chat.id
    tg.tg_username = message.from_user.username
    tg.save()


async def register_user(message: telebot.types.Message, bot: AsyncTeleBot):
    user_id_str = extract_arguments(message.text)
    thread = Thread(target=write_id, args=(message, user_id_str,))
    thread.start()
    thread.join()
    await bot.send_message(message.chat.id,
                           f'You just connected. Visit {HOST_NAME}/accounts/tg/ and apply changes')
