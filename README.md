Dev Installation Guide

Create a virtual Environment
```
$ python -m venv <venv name>

# Activate env for Mac
$ source <venv>/bin/activate

Install packages
$ pip install -r requirements.txt
```

Test server running
```
# Navigate to manage.py directory level in api
$ cd api

# Run server and navigate to local host url
$ python manage.py runserver
```

You might see unapplied migrations when running the runserver command. (TODO)
```
# Changes the database
$ python manage.py migrate

$ python3 manage.py makemigrations models
```


Documentation
```
# Creating admin user for testing purposes
# Navigate to http://127.0.0.1:8000/admin/ in order to fill some data or see the current tables
Username: 'kody'
Password: 'password
# May need to get django-cors-headers
# and add "corsheaders" to settings.py installed apps
# https://www.youtube.com/watch?v=-O2wIkrHLgY&list=PL_c9BZzLwBRKFRIBWEWYCnV4Lk9HE3eYJ&index=33 (9:00 min)
```

