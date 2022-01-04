Game Tracking Web App
=============================
This web app is a personal project made to keep track of what games I am playing,
when I have played them, and how much I have completed. This is meant to be a local server application.

## Building Instructions
These are basic instructions to keep track of basic build commands.

### Setup Environment
This project uses Python 3.10.x. To install packages, use the following command in the
project folder:

```bash
pip install -r requirements.txt
```

### Migrate Changes from App
To migrate changes, perform the following commands in order:

```bash
python manage.py migrate
python manage.py makemigrations game_track_app
python manage.py sqlmigrate game_track_app <four-digit number>
python manage.py migrate
```

### Create Tables for Apps without Migration
To migrate the SQLite tables without further migrations,
perform the following commands:

```bash
python manage.py migrate --run-syncdb
```

## Basic Command Instructions
These are basic instructions that are useful.

### SQLite
To view the SQL console, perform the following command:

```bash
python manage.py dbshell
```

### Run Server
To run the server, perform the following commands:

```bash
python manage.py runserver
```