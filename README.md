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
celery -A TODO worker -P eventlet
```
3. run django app:
```shell
python manage.py runserver 8000
```
## Production
Check this [source](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04). Do:
All daemons need these lines in systemd conf:
```shell
Environment="PG_LOGIN=..."
Environment="PG_PASS=..."
Environment="TG_TOKEN=..."
Environment="DJANGO_SETTINGS_MODULE=TODO.settings"
```
1. Create todo daemon
```shell
...
ExecStart=/path/to/poetry run gunicorn --preload --bind unix:todo.sock TODO.wsgi:application -w 3
...
```
Start this daemon and enable. Check if todo.sock exists.
2. Create nginx conf
```shell

server {
   listen ...
   server_name ...

   location / {
      include proxy_params;
      proxy_pass http://unix:/path/to/project/todo.sock;
   }
   location /static/ {
      root /path/to/project;
   }
}
```
```shell
systemctl restart nginx
```
3. Check if redis server works. Create todo_celery daemon:
```shell
...
ExecStart=/path/to/poetry run celery -A TODO worker -P eventlet -l info
...
```
Start this daemon and enable.
4. Create todo_bot daemon:
```shell
...
ExecStart=/path/to/poetry run python run_polling.py
...
```
Start this daemon and enable. Done!
