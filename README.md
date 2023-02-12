# Json Localization Field

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


## How to use JsonLocalizationField
1. Configure LANGUAGES in settings.py
```python
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
]
```
2. Set default language which is considered as mandatory language
```python
LANGUAGE_CODE = 'en'
```
3. Create form and use JsonLocalizationField for json field
```python
class ArticleForm(forms.Form):
    title = JsonLocalizationField()
```
4. screens