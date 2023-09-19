# Description
Simple task-manager with delayed telegram-notifications
# Install
## Step 1
Preparing server and environment
```shell
git clone https://github.com/gl1tchdev/TODO
```
```shell
cd TODO
```
```shell
apt-get install redis postgresql libpq-dev
```
```shell
sudo -i -u postgres
psql
```
```sql
CREATE DATABASE todo;
```
```shell
exit
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
Check if postgresql connection data is correct in next lines
```python
DATABASES = ...
```
Add your host to
```python
ALLOWED_HOSTS = ...
```
Set up env vars ```PG_LOGIN``` and ```PG_PASS```.<br>
Replace ```STATICFILE_DIRS``` to ```STATIC_ROOT``` if system is linux
## Step 3
```shell
poetry install
```
```shell
poetry shell
python manage.py migrate
python manage.py collectstatic --noinput
```
# Run
## Development
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
## Production
