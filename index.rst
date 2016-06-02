CrossCompute tool framework
===========================
You wrote useful scripts and want folks to use them.

1. Turn your scripts into web apps by writing a configuration file.
2. Host the web apps on your server or `our server <https://crosscompute.com>`_.


Usage
-----
Install. ::

    pip install crosscompute

Configure. ::

    [crosscompute my-fantastic-script]
    command_template = python my_spectacular_script.py {x}

Serve! ::

    crosscompute serve --host 0.0.0.0 --port 4444 --website_name XYZ


Features
--------
- Write your command-line script in any programming language.
- Serve your web app on any operating system.


Topics
------
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


Requests
--------
If you found a bug or want a feature, you can request to have it fixed or implemented.

- `Issues with documentation <https://github.com/crosscompute/crosscompute-docs/issues>`_
- `Issues with examples <https://github.com/crosscompute/crosscompute-examples/issues>`_
- `Issues with tool framework <https://github.com/crosscompute/crosscompute/issues>`_
- `Issues with data types <https://github.com/crosscompute/crosscompute-types/issues>`_

For other requests, you can reach us at support@crosscompute.com.

The CrossCompute tool framework is licensed under the MIT license.
