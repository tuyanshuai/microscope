===============================
microscope
===============================

smart microscope

Quickstart
----------

Run the following commands to bootstrap your environment ::

    git clone https://github.com/tuyanshuai/microscope
    cd microscope
    pip install -r requirements/dev.txt
    cp .env.example .env
    npm install 
    npm run-script build 

You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration ::

    flask db init
    flask db migrate
    flask db upgrade
    npm start


Deployment
----------

To deploy::

    export FLASK_ENV=production
    export FLASK_DEBUG=0
    export DATABASE_URL="<YOUR DATABASE URL>"
    npm run build   # build assets with webpack
    flask run       # start the flask server

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``.


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests/Linter
--------------------

To run all tests, run ::

    flask test

To run the linter, run ::

    flask lint

The ``lint`` command will attempt to fix any linting/style errors in the code. If you only want to know if the code will pass CI and do not wish for the linter to make changes, add the ``--check`` argument.

Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

For a full migration command reference, run ``flask db --help``.

If you will deploy your application remotely (e.g on Heroku) you should add the `migrations` folder to version control.
You can do this after ``flask db migrate`` by running the following commands ::

    git add migrations/*
    git commit -m "Add migrations"

Make sure folder `migrations/versions` is not empty.


