===============================
microscope
===============================

A web-based microscope console

Quickstart
----------

Run the following commands to bootstrap your environment ::
  
    git clone https://github.com/tuyanshuai/microscope
    cd microscope
    pip install -r requirements/dev.txt
    flask run --host=0.0.0.0

When we want to Deployment
----------

To deploy::
    cp .env .env.development
    mv .env.dep .env
    # install apache/ningx
    # Serve
    
Shell
-----

To open the interactive shell, run ::

    flask shell


Running Tests
--------------------

To run all auto tests, run ::

    flask test


Migrations (If modified database  model/strucutre, do this)
----------
Delete Migration template files
    rm -rf migration

Init the database: 
    
    flask db init

Whenever a database migration needs to be made. Run the following commands ::

    flask db migrate

This will generate a new migration script. Then run ::

    flask db upgrade

To apply the migration.

