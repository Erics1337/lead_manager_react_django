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
Create Django App
```
python manage.py startapp leads
```
Setup Database
```
python manage.py makemigrations leads
```
```
python manage.py migrate
```
