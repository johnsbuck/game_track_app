# Instructions
```bash
python manage.py migrate
python manage.py makemigrations game_track_app
python manage.py sqlmigrate game_track_app 0001
python manage.py migrate
```

## Create Tables for Apps without Migration
```bash
python manage.py migrate --run-syncdb
```