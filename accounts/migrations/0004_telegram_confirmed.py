# Generated by Django 4.2.5 on 2023-09-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_telegram_tg_chat_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegram',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]