Example Falcon App
=======================

Build
-----
Make it with Travis-CI

.. image:: https://travis-ci.org/altereg0/3EQ4MRKk.svg?branch=master
    :target: https://travis-ci.org/altereg0/3EQ4MRKk

Installation
------------

From the cloned source, execute:

.. code-block:: shell

    pip install -e .

Running
-------

Once installed you can run the service using the ``falcon-example`` command.

.. note::

    The service connects to a MySQL database. You'll need to edit the service
    config in ``etc/example/config.yml`` to match your configuration.

Running Tests
-------------

Install test requirements

.. code-block:: shell

    pip install -r dev-requirements.txt

Execute the tests by running the ``tox`` command:

Alter
_____
