# Generated by Django 4.2.5 on 2023-09-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_telegram_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegram',
            name='tg_username',
            field=models.CharField(default=None, null=True),
        ),
    ]