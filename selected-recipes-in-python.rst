Selected recipes in Python
==========================
Although we have used Python for our examples, you can easily adapt these recipes to command-line scripts written in other programming languages.

.. todo:: Write examples using other programming languages.


Capture standard streams
------------------------
In the simplest case, you have a command-line script and you want to capture its standard output.  Here is an example of such a script.

.. literalinclude:: examples/python/divide-floats/run.py
   :language: python

Running the script produces the following output.  ::

    $ python run.py 4 5
    4 divided by 5 is 0.8

To wrap the script in a web interface, we write a configuration file.

.. literalinclude:: examples/python/divide-floats/cc.ini
   :language: ini


Specify tool name
`````````````````
The configuration file must end with the extension ``.ini`` and contain a section that starts with the word ``crosscompute``, optionally followed by the name of the tool.

.. code-block:: ini

    [crosscompute our-simple-one-function-calculator]

If you do not specify a tool name, then the name of the tool will be the name of the folder containing the configuration file.


.. _specify_command_line_arguments:

Specify command-line arguments
``````````````````````````````
The most important option in the configuration file is the ``command_template``, which tells CrossCompute how to run your script.

Here, we use ``python`` to execute ``run.py`` with ``x`` and ``y`` as arguments.

.. literalinclude:: examples/python/divide-floats/cc.ini
   :language: ini
   :lines: 2

If your command is long, you can split it across multiple lines.

.. code-block:: ini

    command_template = bash script-with-many-arguments.sh
        {first_argument}
        {second_argument}
        {third_argument}


Capture standard streams
````````````````````````
CrossCompute parses but does not save standard output or standard error from the script, unless requested to do so explicitly.

.. literalinclude:: examples/python/divide-floats/cc.ini
   :language: ini
   :lines: 3-4


Specify default values for arguments
````````````````````````````````````
When executed without arguments, ``crosscompute run`` uses the default values specified in the configuration file, which can save time during development.

.. literalinclude:: examples/python/divide-floats/cc.ini
   :language: ini
   :lines: 5-6

Additionally, ``crosscompute serve`` uses the default values to populate the tool form.  If an argument name ends with ``_path`` and a default file path is specified, the web app will show the contents of the file in the form.  For example, this configuration file

.. literalinclude:: examples/python/get-size/cc.ini
   :language: ini

will render the following form.

.. image:: _static/get-size-tool.png


Run tool
````````
First, check that the application development framework is installed on your system.  ::

    $ crosscompute
    usage: crosscompute {serve,run} ...
    crosscompute: error: too few arguments

Then execute ``crosscompute run`` in the parent folder or same folder as your configuration file.  ::

    $ crosscompute run
    [tool_definition]
    tool_name = divide-floats
    configuration_path = ~/Experiments/divide-floats/cc.ini
    command = python run.py 10 3

    [result_arguments]
    x = 10
    y = 3
    target_folder = /tmp/divide-floats/results/1

    [standard_output]
    10 divided by 3 is 3.33333333333

    [result_properties]
    standard_output = 10 divided by 3 is 3.33333333333
    execution_time_in_seconds = 0.0374681949615

The ``target_folder`` contains the result generated from this run.  Each subsequent run will save the result in a new ``target_folder``.  ::

    $ ls /tmp/divide-floats/results/1
    result.cfg  standard_output.log

If there is more than one tool, you will need to specify the tool name explicitly.  ::

    $ crosscompute run divide-floats


Override default values
```````````````````````
Sometimes, you might want to override default argument values.  Use ``--help`` to show the required syntax.  ::

    $ crosscompute run --help
    usage: divide-floats [-h] [--x X] [--y Y]

    optional arguments:
    -h, --help  show this help message and exit
    --x X
    --y Y

If our script terminates unexpectedly, ``crosscompute run`` will show any errors.  In this case, the standard error stream is rendered twice because ``show_standard_error = True``.  ::

    $ crosscompute run --y 0
    [tool_definition]
    tool_name = divide-floats
    configuration_path = ~/Experiments/divide-floats/cc.ini
    command = python run.py 10 0

    [result_arguments]
    x = 10
    y = 0
    target_folder = /tmp/divide-floats/results/2

    [standard_error]
    Traceback (most recent call last):
      File "run.py", line 3, in <module>
        print('{} divided by {} is {}'.format(x, y, float(x) / float(y)))
    ZeroDivisionError: float division by zero

    [result_properties]
    return_code = 1
    standard_error = 
    Traceback (most recent call last):
      File "run.py", line 3, in <module>
        print('{} divided by {} is {}'.format(x, y, float(x) / float(y)))
    ZeroDivisionError: float division by zero
    execution_time_in_seconds = 0.166897058487


Serve tool
``````````
Once you are satisfied that the script is configured properly, execute ``crosscompute serve`` to serve the web app.  ::

    $ crosscompute serve

.. image:: _static/divide-floats-tool.png

Click **Run** to see the result.

.. image:: _static/divide-floats-result.png


Save output files
-----------------
The ``target_folder`` argument is a special keyword that specifies the folder where your script can save files for the user to download.

.. literalinclude:: examples/python/save-text/cc.ini
   :language: ini

If your script saves files in the folder, then the user will have access to those files by downloading the archive on the result page.

.. literalinclude:: examples/python/save-text/run.py
   :language: python

Run the script by typing ``crosscompute run`` in the same folder as ``cc.ini``.  ::

    $ crosscompute run
    [tool_definition]
    tool_name = save-text
    configuration_path = ~/Experiments/save-text/cc.ini
    command = python run.py /tmp/save-text/results/1

    [result_arguments]
    target_folder = /tmp/save-text/results/1

    [result_properties]
    execution_time_in_seconds = 0.0495231151581

    $ ls /tmp/save-text/results/1
    result.cfg  xyz.txt

Serve the script by typing ``crosscompute serve`` in the same folder as ``cc.ini``.  ::

    $ crosscompute serve

Run the tool, then click ``Download`` to receive an archive containing the result configuration as well as any files saved in the ``target_folder``.

.. image:: _static/save-text-result.png

Additionally, the tool will be able to render the content of those files for selected data types (see :ref:`specify_data_types_for_result_properties`).  Here is a slightly more involved example that counts the number of each non-whitespace character in a text file.

.. literalinclude:: examples/python/count-characters/cc.ini
   :language: ini

The script tells CrossCompute to render the output file as a table by printing a statement in the form ``xyz_table_path = abc.csv``.

.. literalinclude:: examples/python/count-characters/run.py
   :language: python

Running the tool using ``crosscompute serve`` renders the desired table.

.. image:: _static/count-characters-result.png


Specify data types for tool arguments
-------------------------------------
Specifying the data type of a tool argument provides the following benefits.

- The script can assume that an argument matches its specified data type.  For example, the script below can assume that its first argument is an integer because the framework performs basic integer validation before running the script.
- The corresponding web application renders an appropriate query for the argument in the form.

.. image:: _static/load-inputs-tool.png

The suffix of a tool argument determines its data type.  Specify tool arguments in the ``command_template`` by enclosing argument names in curly brackets (see :ref:`specify_command_line_arguments`).  In the configuration file below, the arguments are ``some_count`` (integer), ``a_text_path`` (text), ``a_table_path`` (table).

.. literalinclude:: examples/python/load-inputs/cc.ini
   :language: ini

Only the configuration file ``command_template`` is relevant when determining tool argument data types.  The script does not have to use the same argument names.

.. literalinclude:: examples/python/load-inputs/run.py
   :language: python

Install the relevant data type plugins.  CrossCompute matches argument name endings to suffixes registered by installed data types.  ::

    pip install -U crosscompute-integer
    pip install -U crosscompute-text
    pip install -U crosscompute-table

You can also register your own data type plugins.  For examples on how to write data type plugins, please see https://github.com/crosscompute/crosscompute-types.


.. _specify_data_types_for_result_properties:

Specify data types for result properties
----------------------------------------
Similarly, specifying the data type of a result property provides the following benefits.

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
