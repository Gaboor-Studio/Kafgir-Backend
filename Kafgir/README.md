# How to use?

### 1) Make migrations

To create migrations run:

```
python3 manage.py makemigrations
```

And to perform migrations run:

```
python3 manage.py migrate
```

### 2) Run Server

To start server run the following code:

```
python3 manage.py runserver
```

It will be deployed in 8000 port by default. to change the port or host you can specify them after runserver command:

```
python3 manage.py runserver 0.0.0.0:8585
```

