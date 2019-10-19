===============================
microscope
===============================

smart microscope

Quickstart
----------

Run the following commands to bootstrap your environment ::

    export FLASK_ENV=development
    export FLASK_DEBUG=1
    git clone https://github.com/tuyanshuai/microscope
    cd microscope
    pip install -r requirements/dev.txt
    flask run



When we want to Deployment
----------

To deploy::

    export FLASK_ENV=production
    export FLASK_DEBUG=0   
    # install apache/ningx
    # TODO test the app by apache.nginx

Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Running Tests
--------------------

To run all tests, run ::

    flask test


Migrations
----------

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

