.. _installation_instructions:

Installation instructions
=========================
To separate CrossCompute packages from system packages, we recommend using virtualenv_ to prepare an isolated environment.

::

    VIRTUAL_ENV=~/.virtualenvs/crosscompute

    # Prepare isolated environment
    virtualenv $VIRTUAL_ENV

    # Activate isolated environment 
    source $VIRTUAL_ENV/bin/activate

    # Install application development framework
    pip install -U crosscompute

    # Install data type plugins
    pip install -U crosscompute-integer
    pip install -U crosscompute-text
    pip install -U crosscompute-table
    pip install -U crosscompute-image
    pip install -U crosscompute-geotable


.. _virtualenv: https://virtualenv.readthedocs.org
