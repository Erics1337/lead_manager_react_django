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

## Create Frontend
```
cd leadmanager
python manage.py startapp frontend
mkdir -p ./frontend/src/components
mkdir -p ./frontend/{static,templates}/frontend
```
src is where all react stuff goes
templates handles the html file that gets loaded (the single page)
static is the compiled js and css
### Install react, webpack, babel
```
cd ..
npm init -y
npm i -D webpack webpack-cli
npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties
npm i react react-dom prop-types
```
In order to use these presets and plugins, you need to create a .babelrc file
Create a webpack.config.js file to load babel loader and presets that will alllow to transpile code
Add script to dev command in package.json to run webpack and compile js from one specified folder to the next
```
  "scripts": {
    "dev": "webpack --mode development ./leadmanager/frontend/src/index.js --output-path ./leadmanager/frontend/static/frontend/main.js",
    "build": "webpack --mode development ./leadmanager/frontend/src/index.js --output-path ./leadmanager/frontend/static/frontend/main.js"
  },
Create frontend/src/index.js
Create frontend/src/components/App.js
Create frontend/templates/frontend/index.html and
include the django template to inject the react app and other static assets
```
    <div id="app"></div>
    <script src="{{ asset('js/app.js') }}"></script>
    <script src="{% static 'frontend/main.js' %}"></script>
```
In frontend/views.py create a view method that will point to the index file to inject react into
Link a URL to the view
Include the frontend urls into the main urls file