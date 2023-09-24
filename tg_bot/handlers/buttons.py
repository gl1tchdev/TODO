from telebot.types import CallbackQuery
from telebot.async_telebot import AsyncTeleBot
from todolist.models import Task
from threading import Thread


def mark_done(task_id: int):
    task = Task.objects.get(pk=task_id)
    task.done = True
    task.save()


async def handle_buttons(callback: CallbackQuery, bot: AsyncTeleBot):
    data = callback.data
    message_id = callback.message.id
    await bot.edit_message_reply_markup(chat_id=callback.from_user.id, message_id=message_id, reply_markup=None)
    await bot.answer_callback_query(callback_query_id=callback.id)
    if data == 'pass':
        return
    thread = Thread(target=mark_done, args=(int(callback.data),))
    thread.start()
    thread.join()