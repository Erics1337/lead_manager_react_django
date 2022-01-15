# Lead Manager

> Full stack Django/React/Redux app that uses token based authentication with Knox.

## Quick Start

```bash
# Install dependencies
npm install

# Serve API on localhost:8000
python leadmanager/manage.py runserver

# Run webpack (from root)
npm run dev

# Build for production
npm run build
```


## Setup
```
pip3 install pipenv
```
```
pipenv shell
```
```
pipenv install django djangorestframework django-rest-knox
```


## Steps to set up rest_api called leads
1. Create a new Django app 
```
python manage.py startapp leads
```
2.  Create leads Model
```
python manage.py makemigrations leads
```
3. Migrate
```
python manage.py migrate
```
4. Create Serializer leads/serializers.py
5. Create API viewset leads/api.py
6. Edit root urls file leadManager/urls.py to include leads/urls.py
7. Create leads/urls.py to register routes from api viewset
8. Run server
```
python manage.py runserver
```
