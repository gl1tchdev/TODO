from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    date_time = models.DateTimeField()
    sent = models.BooleanField(default=False)


class Task(models.Model):
    title = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    notification = models.OneToOneField(Notification, on_delete=models.CASCADE, default=None, null=True)
