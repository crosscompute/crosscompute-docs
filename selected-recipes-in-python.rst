Selected recipes in Python
==========================
Although we have used Python for our examples, you can easily adapt these recipes to command-line scripts written in other programming languages.

.. todo:: Write examples using other programming languages.


Capture standard streams
------------------------
In the simplest case, you have a command-line script and you want to capture its standard output.  Here is an example of such a script.

.. literalinclude:: recipes/python/capture-standard-streams/run.py
   :language: python

Running the script produces the following output.
::

    $ python run.py 4 5
    4 divided by 5 is 0.8

To wrap the script in a web interface, we write a configuration file in the same folder as the script.

.. literalinclude:: recipes/python/capture-standard-streams/cc.ini
   :language: ini

.. todo:: Explain command_template
.. todo:: Explain how to capture standard streams
.. todo:: Define default values for arguments
.. todo:: Cover run
.. todo:: Override default values
.. todo:: Cover serve


Save output files
-----------------
.. todo:: Show example script
.. todo:: Show configuration file
.. todo:: Save output files in target_folder


Specify data types for input arguments
--------------------------------------
.. todo:: Show example script
.. todo:: Show configuration file
.. todo:: Specify data types for input arguments using suffixes


Specify data types for output properties
----------------------------------------
.. todo:: Show example script
.. todo:: Show configuration file
.. todo:: Print properties to standard output
.. todo:: Specify data types for output properties using suffixes


Log errors
----------
.. todo:: Show example script
.. todo:: Show configuration file


Specify dependencies
--------------------
.. todo:: Show example script
.. todo:: Show configuration file


Specify help popovers
---------------------
.. todo:: Specify help popovers for arguments and properties


Serve multiple apps
-------------------
.. todo:: Discuss configuration options when serving multiple apps


Show images
-----------
.. todo:: Verify installation
.. todo:: Show example script
.. todo:: Show configuration file


Show tables
-----------
.. todo:: Verify installation
.. todo:: Show example script
.. todo:: Show configuration file


Show maps
---------
.. todo:: Verify installation
.. todo:: Show example script
.. todo:: Show configuration file
.. todo:: Show how various column names render different styles
