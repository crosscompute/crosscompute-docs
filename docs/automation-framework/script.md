CrossCompute will run your code as specified in your configuration file. Your code can be a Python function, a Python script, a Jupyter notebook or a Bash command. Your code can be in any programming language such as R or Julia.

```yaml
# Python function
function: run.plot

# Python script
command: python run.py

# Jupyter notebook
command: python -c "$(jupyter nbconvert run.ipynb --to script --stdout)"

# Bash command
command: julia run.jl
```

CrossCompute needs a way to tell your script where to load input variables and where to save output variables. You have two options for configuring your script:

- Option 1: Use command-line arguments
- Option 2: Use environment variables

### Command-Line Arguments

You can use command-line arguments to specify the input, output, log, debug folders.

```yaml
command: python x.py {input_folder} {output_folder} {log_folder} {debug_folder}
```

Here is an example of a simple script that uses command-line arguments to define a web-based tool.

**Script (`run.py`)**

```python
import json
from os.path import join
from sys import argv


# Get folder paths from command-line arguments
input_folder, output_folder = argv[1:]


# Load input variables from input folder
variables = json.load(open(join(input_folder, 'variables.dictionary'), 'rt'))


# Perform calculation
c = variables['a'] + variables['b']


# Save output variables to output folder
json.dump({
    'c': c,
}, open(join(output_folder, 'variables.dictionary'), 'wt'))
```

**Configuration (`automate.yml`)**

```yaml
---
# version of crosscompute
crosscompute: 0.9.0

# name of your automation
name: Add Numbers

# version of your automation
version: 0.1.0

# input configuration
input:

  # input variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script loads the variable,
  #   relative to the input folder
  variables:
    - id: a
      view: number
      path: variables.dictionary
    - id: b
      view: number
      path: variables.dictionary

# output configuration
output:

  # output variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script saves the variable,
  #   relative to the output folder
  variables:
    - id: c
      view: number
      path: variables.dictionary

# tests configuration
# - folder that contains an input subfolder with paths for
#   input variables that define a specific test
tests:
  - folder: tests/integers
  - folder: tests/floats

# script configuration
script:

  # folder where your script should run
  folder: .

  # command to use to run your script
  command: python run.py {input_folder} {output_folder}
```

### Environment Variables

CrossCompute will define the following environment variables before running your script:

- ``CROSSCOMPUTE_INPUT_FOLDER``: Your script should expect to find input variables saved to this folder at the relative path specified in the configuration file.
- ``CROSSCOMPUTE_OUTPUT_FOLDER``: Your script should save output variables to this folder at the relative path specified in the configuration file.
- ``CROSSCOMPUTE_LOG_FOLDER``: Your script can save log variables to this folder at the relative path specified in the configuration file. These log variables will be visible to the user.
- ``CROSSCOMPUTE_DEBUG_FOLDER``: Your script can save debug variables to this folder at the relative path specified in the configuration file. These debug variables will not be visible to the user.

Here is an example of a simple script that uses environment variables to define a web-based tool. Note that you will most likely use environment variables if your script is a Jupyter notebook.

**Script (`run.py`)**

```python
import json
from os import environ
from os.path import join


# Get folder paths from environment variables
input_folder = environ.get(
    'CROSSCOMPUTE_INPUT_FOLDER', 'tests/integers/input')
output_folder = environ.get(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'tests/integers/output')


# Load input variables from input folder
variables = json.load(open(join(input_folder, 'variables.dictionary'), 'rt'))


# Perform calculation
c = variables['a'] + variables['b']


# Save output variables to output folder
json.dump({
    'c': c,
}, open(join(output_folder, 'variables.dictionary'), 'wt'))
```

**Configuration (`automate.yml`)**

```yaml
---
# version of crosscompute
crosscompute: 0.9.0

# name of your automation
name: Add Numbers

# version of your automation
version: 0.1.0

# input configuration
input:

  # input variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script loads the variable,
  #   relative to the input folder
  variables:
    - id: a
      view: number
      path: variables.dictionary
    - id: b
      view: number
      path: variables.dictionary

# output configuration
output:

  # output variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script saves the variable,
  #   relative to the output folder
  variables:
    - id: c
      view: number
      path: variables.dictionary

# tests configuration
# - folder that contains an input subfolder with paths for
#   input variables that define a specific test
tests:
  - folder: tests/integers
  - folder: tests/floats

# script configuration
script:

  # folder where your script should run
  folder: .

  # command to use to run your script
  command: python run.py
```

