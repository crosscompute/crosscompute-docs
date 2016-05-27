Installation instructions
=========================
To separate CrossCompute packages from system packages, we recommend using `virtualenv <https://virtualenv.readthedocs.org>`_ to prepare an isolated environment. ::

    VIRTUAL_ENV=~/.virtualenvs/crosscompute

    # Prepare isolated environment
    virtualenv $VIRTUAL_ENV

    # Activate isolated environment 
    source $VIRTUAL_ENV/bin/activate

    # Install application framework and data types
    pip install -U crosscompute crosscompute-types


Troubleshooting
---------------


Fedora
~~~~~~


Ubuntu
~~~~~~


The program 'pip' is currently not installed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ``pip`` command installs Python packages. ::

    # Python 2
    sudo apt install -y python-pip python-virtualenv
    VIRTUAL_ENV=~/.virtualenvs/python2
    virtualenv -p `which python2` $VIRTUAL_ENV
    source $VIRTUAL_ENV/bin/activate

    # Python 3
    sudo apt install -y python3-pip python3-virtualenv
    VIRTUAL_ENV=~/.virtualenvs/python3
    virtualenv -p `which python3` $VIRTUAL_ENV
    source $VIRTUAL_ENV/bin/activate


Mac OS
~~~~~~


pip: command not found
^^^^^^^^^^^^^^^^^^^^^^
1. Install `brew <http://brew.sh/>`_ ::

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

2. Install Python 2 ::

    brew install python
    pip2 install -U pip virtualenv
    VIRTUAL_ENV=~/.virtualenvs/python2
    virtualenv -p `which python2` $VIRTUAL_ENV
    source $VIRTUAL_ENV/bin/activate

3. Install Python 3 ::

    brew install python3
    pip3 install -U pip virtualenv
    VIRTUAL_ENV=~/.virtualenvs/python3
    virtualenv -p `which python3` $VIRTUAL_ENV
    source $VIRTUAL_ENV/bin/activate


Windows
~~~~~~~


'virtualenv' is not recognized as an internal or external command, operable program or batch file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Run Command Prompt with administrative privileges (see `IOError: [Errno 13] Permission denied`_).
2. Change to the directory of your target Python installation ::

    cd "\Program Files\Python27"
    cd "\Program Files\Python35"

3. Upgrade ``pip`` ::

    python -m pip install -U pip

4. Install ``virtualenv`` ::

    Scripts\pip.exe install -U virtualenv
    Scripts\virtualenv.exe VirtualEnvs\CrossCompute

5. Install packages in your new ``virtualenv`` ::

    VirtualEnvs\CrossCompute\Scripts\activate
    pip install -U crosscompute crosscompute-types


IOError: [Errno 13] Permission denied
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run Command Prompt with administrative privileges.

- For Windows 8+, right-click on the Windows Start icon and select Command Prompt (Admin).


Unable to find vcvarsall.bat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
One of the packages that you are installing is trying to compile a C/C++ dependency and is looking for an appropriate compiler.

- For Python 3.5, you can install `Visual C++ Build Tools 2015 <http://go.microsoft.com/fwlink/?LinkId=691126>`_.
- For Python 2.7, you can install `Microsoft Visual C++ Compiler <https://www.microsoft.com/download/details.aspx?id=44266>`_.

Please see https://blogs.msdn.microsoft.com/pythonengineering/2016/04/11/unable-to-find-vcvarsall-bat/ for more information.
