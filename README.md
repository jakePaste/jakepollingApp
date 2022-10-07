# pollingApp
A short django-based app to provide admin permissions, polling results on specific questions, and etc,. 

# For setting environment like npm init
pip3 install pipenv

# Creating Virtual Environment
pipenv shell

# Install Django
pipenv install django

# Create project
django-admin startproject pollApp
cd pollApp

# Run server on http: 127.0.0.1:8000 (ctrl+break to stop)
python manage.py runserver

# Run initial migrations
python manage.py migrate

# Create polls app
python manage.py startapp polls

# Create polls migrations
python manage.py makemigrations polls

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Create pages app
python manage.py startapp pages
