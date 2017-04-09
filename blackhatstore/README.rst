.. 

blackhatstore
======================

Quickstart
----------

To bootstrap the project::

    virtualenv blackhatstore
    source blackhatstore/bin/activate
    cd path/to/blackhatstore/repository
    pip install -r requirements.pip
    pip install -e .
    cp blackhatstore/settings/local.py.example blackhatstore/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
