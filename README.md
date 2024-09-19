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


