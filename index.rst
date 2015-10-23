.. CrossCompute documentation master file, created by
   sphinx-quickstart on Thu Aug 13 15:54:20 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CrossCompute 20151005
=====================
1. Publish your computational model as a web application.
2. Get paid each time your computational model runs.

Instructions
------------
Prepare development environment. ::

    # Install command line scripts
    pip install -U crosscompute

    # Install data type plugins
    pip install -U crosscompute-integer
    pip install -U crosscompute-text
    pip install -U crosscompute-table

Write your computational script. ::

    vim run.py

        # http://stackoverflow.com/questions/16007204/factorizing-a-number-in-python
        import sys
        from math import sqrt

        integer = int(sys.argv[1])
        minimum_factor = 2
        factors = []
        while integer > 1:
            for i in xrange(minimum_factor, int(sqrt(integer + 0.05)) + 1):
                if integer % i == 0:
                    integer /= i
                    minimum_factor = i
                    factors.append(i)
                    break
            else:
                if integer > 1:
                    factors.append(integer)
                    break
        print('factors = %s' % factors)
        print('unique_factor_count = %s' % len(set(factors)))

Configure your computational script. ::

    vim cc.ini

        [crosscompute]
        command_template = python2.7 run.py {x_integer}
        x_integer.value = 33

    crosscompute run

Test your web application locally. ::

    crosscompute serve

Share your web application. ::

    https://crosscompute.com

Supported data types
--------------------
- string (default)
- path
- text
- integer
- table
- image (pending)
- audio (pending)
- video (pending)
- geotable (pending)
- geoimage (pending)
- geoaudio (pending)
- geovideo (pending)

Supported architectures
-----------------------
- CPU
- GPU (pending)

Examples
--------
.. toctree::
    :maxdepth: 2

    add-integers
    find-prime-factors
    count-words
    convert-timestamps
    count-buildings
