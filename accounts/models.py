from django.db import models
from django.contrib.auth.models import User


class Telegram(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tg_chat_id = models.IntegerField(default=None, null=True)
    tg_random_salt = models.CharField(default=None, null=True)
    confirmed = models.BooleanField(default=False)
    tg_username = models.CharField(default=None, null=True)
