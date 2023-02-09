# django-json-text-widget

## Setup

1. Install pipenv
```shell
pip install pipenv
```
2. Install Dependencies
```shell
pipenv install
```
3. Copy .env.example and rename it to .env
4. Update database credentials in .env file
```dotenv
DATABASE_URL=psql://postgres:postgres@localhost:5432/django-json-text-widget
```
5. Run migrations
```shell
$ ./manage.py migrate
```
6. Run server
```shell
$ ./manage.py runserver
```
7. 