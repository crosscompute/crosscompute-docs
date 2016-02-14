CrossCompute application development framework
==============================================
You wrote useful scripts and want folks to use them.

1. Turn your scripts into web applications by writing a configuration file.
2. Host the web applications on CrossCompute_ or your own server.

::

    pip install crosscompute

    cat > run.py << EOF
    import sys
    print('y = %s' % len(sys.argv[1]))
    EOF

    cat > cc.ini << EOF
    [crosscompute get-length]
    command_template = python run.py {x}
    EOF

    crosscompute serve


Features
--------
- Write your command-line script in any programming language.
- Serve your application on any operating system.


References
----------
.. toctree::
   :maxdepth: 2

   installation-instructions
   selected-recipes-in-python
   feature-requests


License
-------
The CrossCompute Application Development Framework is licensed under the MIT license.


.. _CrossCompute: https://crosscompute.com
