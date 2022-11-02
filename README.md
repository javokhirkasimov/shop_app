# Shop App

## Overview

This is simple API for a mobile application in which a customer's field worker will perform outlet visits.
Uses latest Django with Python version 3.9

## Running The Project

First you have to activate your virtual environment and install dependencies with command:
```bash
pip install -r requirements.txt
```
Then configure your database config
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
and run these commands:
```bash
python manage.py migrate
python manage.py runserver
```

## Dependencies
* [Django](https://docs.djangoproject.com/en/4.1/)
* [Django Rest Framework](https://www.django-rest-framework.org/)