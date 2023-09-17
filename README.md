# Description
Simple task-manager with delayed telegram-notifications
# Install
## Step 1
First of all you need to install: Postgresql 15, redis 3.0.504, poetry. 
```shell
git clone https://github.com/gl1tchdev/TODO
```
```shell
cd TODO
```
## Step 2
Create telegram bot and open file ```TODO/settings.py```:<br>
set up environment variable ```TG_TOKEN``` and save it
paste tg bot link to settings:
```
TELEGRAM_BOT_LINK = 'paste link here'
```
Change next lines too:<br>
```
HOST_NAME = 'full address of application'
```
```
REDIS_URL = 'url of redis-server'
```
Create db "todo" and check if postgresql connection data is correct in next lines
```python
DATABASES = ...
```
Also set up env vars ```PG_LOGIN``` and ```PG_PASS```
## Step 3
```shell
poetry install
```
```shell
poetry shell
```
After all you need to
1. run polling for tg registration app: 
```shell
python run_polling.py
```
2. run celery app and redis-server for tg notifications: 
```shell
redis-server
```
```shell
python -m celery -A TODO worker -P eventlet
```
3. run django app:
```shell
python manage.py runserver 8000
```