from tg_bot.main import send_message
from celery import shared_task
from accounts.models import Telegram
from .models import Task
from TODO.settings import HOST_NAME
from telebot.formatting import format_text, hbold, hunderline, hlink


@shared_task()
def notify_user(user_id: int, task_id: int) -> bool:
    tg = Telegram.objects.get(user_id=user_id)
    chat_id = tg.tg_chat_id
    task = Task.objects.get(pk=task_id)
    task_title = hbold(task.title)
    task_time = hunderline(str(task.notification.date_time))
    task_text = f'Reminder! You need to do {task_title} at {task_time}.\n\nYou received this message ' \
                f'because you set reminder at {HOST_NAME}. You can unsubscribe {hlink("here", HOST_NAME + "/tg")}'
    send_message(chat_id, task_text)
    task.notification.sent = True
    task.notification.save()
    task.save()
    return True


