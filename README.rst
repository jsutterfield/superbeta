===================
web-based superbeta
===================
This is the repository for the web-based version of superbeta

Installing/running
==================
To install run the following commands

1. Clone Repo from bitbucket

2. Install using setup.py
::
    python setup.py install

3. Start development server
::
    python manage.py runserver

4. You'll find the app running on http://127.0.0.1:8000/

Using South to migrate
======================
South is a database migration library which is used whenever changes/additions are made to 
the models. Django will create new tables as models are created, but will not alter tables
when a model is changed - this is where South comes in. South allows you to change a model
(eg, add a property, change an existing properties datatype), and will run the necessary
SQL statements to sync the tables with the models. Full documentation is available at 
http://south.readthedocs.org/en/latest/index.html

1. Make some changes to the model in the app *appname*

2. Create a migration

If you're changing an existing model use
::
    python manage.py schemamigration *appname* --auto

however, if you're creating an entirely new model you'll want
::
    python manage.py schemamigration *appname* --initial
    python manage.py migrate *appname* --fake

3. Migrate your changes
::
    python manage.py migrate appname

Note: Each app needs to have migrations created and applied individually. For example:
::
    python manage.py schemamigration climbs --auto
    python manage.py migrate climbs
    python manage.py schemamigration users --auto
    python manage.py migrate superbeta
    python manage.py schemamigration superbeta --auto
    python manage.py migrate users
