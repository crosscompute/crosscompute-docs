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

.. raw:: html

    <iframe width="520" height="304" src="https://www.youtube.com/embed/iGkYjzguczA"></iframe> 
    <iframe width="520" height="304" src="https://www.youtube.com/embed/kgIEwMnOoJc"></iframe> 
    <iframe width="520" height="304" src="https://www.youtube.com/embed/7eAj9eTUfZY"></iframe> 
    <iframe width="520" height="304" src="https://www.youtube.com/embed/HmcXOpE1Ukk"></iframe> 
    <iframe width="520" height="304" src="https://www.youtube.com/embed/r6YXbvgVfS4"></iframe> 


Feature requests
----------------
If you found a bug or want a feature, you can request to have it fixed or implemented.

- `Issues with documentation <https://github.com/crosscompute/crosscompute-docs/issues>`_
- `Issues with examples <https://github.com/crosscompute/crosscompute-examples/issues>`_
- `Issues with application development framework <https://github.com/crosscompute/crosscompute/issues>`_
- `Issues with data type plugins <https://github.com/crosscompute/crosscompute-types/issues>`_

For other requests, you can reach us at support@crosscompute.com.


License
-------
The CrossCompute Application Development Framework is licensed under the MIT license.


.. _CrossCompute: https://crosscompute.com
