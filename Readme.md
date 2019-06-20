# Flask

This project creates a simple flask web app

## Running the application

To start the application use these commands

```bash
set FLASK_APP=microblog.py
flask run
```

Added Database using Flask-Migrate command

```bash
flask db init
flask db migrate -m "users table"
flask db upgrade
```

This was used initially to create a database migration to allow for the 
database to be upgraded or downgraded as changes occur

flask db migrate does not make any
changes to the database it just generates
a migration script. To apply the changes
to the database, the flask db upgrade command must be used

You can also return to before the last migration using this command

```
flask db downgrade
```