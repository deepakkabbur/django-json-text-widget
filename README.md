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
7. Create Super User
```shell
$ ./mange.py createsuperuser
```
Fill details and remember credentials 
8. Run server
```shell
./manage.py runserver
```
Visit [admin](http://127.0.0.1:8000/admin) and enter credentials
9. 