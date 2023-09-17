import django
import asyncio

django.setup()

from tg_bot.main import async_bot_instance

if __name__ == '__main__':
    asyncio.run(async_bot_instance.polling())
