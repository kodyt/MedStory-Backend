Dev Installation Guide

Create a virtual Environment
```
$ python -m venv <venv name>

# Activate env for Mac
$ source <venv>/bin/activate

Install packages
$ pip install -r requirements.txt
```

Run server to make REST API calls from frontend
```
# Navigate to manage.py directory level in api
$ cd api

# Run server and navigate to local host url
$ python manage.py runserver

```


You might see unapplied migrations when running the runserver command. (TODO)
```
# When changing models.py, views.py, or serializers.py make migrations to reflect changes in the database (Do both commands in this order)
$ python3 manage.py makemigrations

$ python manage.py migrate
```


Documentation
```
# Creating admin user for testing purposes
# Navigate to http://127.0.0.1:8000/admin/ in order to fill some data or see the current tables
Username: 'kody'
Password: 'password

# Django tutorial reference
# https://www.youtube.com/watch?v=-O2wIkrHLgY&list=PL_c9BZzLwBRKFRIBWEWYCnV4Lk9HE3eYJ&index=33
```

