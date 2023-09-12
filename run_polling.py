import os, django
import asyncio

django.setup()

from tg_bot.main import bot

if __name__ == '__main__':
    asyncio.run(bot.polling())
