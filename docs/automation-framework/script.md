CrossCompute will run your code as specified in your configuration file. Your code can be a Python script, a Jupyter notebook or a Bash command. Your code can be in any programming language such as R or Julia.

```yaml
# Python script
path: run.py

# Jupyter notebook
path: run.ipynb

# Bash command
command: julia run.jl
```

CrossCompute needs a way to tell your scripts where to load input variables and where to save output variables. You have two options for configuring your scripts:

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
from pathlib import Path
from sys import argv

input_folder, output_folder = [Path(_) for _ in argv[1:]]
with (input_folder / 'variables.dictionary').open('rt') as f:
    variables = json.load(f)
c = variables['a'] + variables['b']
with (output_folder / 'variables.dictionary').open('wt') as f:
    json.dump({'c': c}, f)
```

**Configuration (`automate.yml`)**

```yaml
---
crosscompute: 0.9.2
name: Add Numbers
version: 0.1.0
input:
  variables:
    - id: a
      view: number
      path: variables.dictionary
    - id: b
      view: number
      path: variables.dictionary
output:
    - id: c
      view: number
      path: variables.dictionary
batches:
  - name: '{a} + {b}'
    folder: batches/{a}-{b}
    configuration:
      path: datasets/batches.csv
scripts:
  - command: python run.py {input_folder} {output_folder}
```

### Environment Variables

CrossCompute will define the following environment variables before running your scripts:

- ``CROSSCOMPUTE_INPUT_FOLDER``: Your script should expect to find input variables saved to this folder at the relative path specified in the configuration file.
- ``CROSSCOMPUTE_OUTPUT_FOLDER``: Your script should save output variables to this folder at the relative path specified in the configuration file.
- ``CROSSCOMPUTE_LOG_FOLDER``: Your script can save log variables to this folder at the relative path specified in the configuration file. These log variables will be visible to the user.
- ``CROSSCOMPUTE_DEBUG_FOLDER``: Your script can save debug variables to this folder at the relative path specified in the configuration file. These debug variables will not be visible to the user.

Here is an example of a simple script that uses environment variables to define a web-based tool. Note that you will most likely use environment variables if your script is a Jupyter notebook.

**Script (`run.py`)**

```python
import json
from os import getenv
from pathlib import Path

input_folder = getenv(
    'CROSSCOMPUTE_INPUT_FOLDER', 'tests/integers/input')
output_folder = getenv(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'tests/integers/output')
with (input_folder / 'variables.dictionary').open('rt') as f:
    variables = json.load(f)
c = variables['a'] + variables['b']
with (output_folder / 'variables.dictionary').open('wt') as f:
    json.dump({'c': c}, f)
```

**Configuration (`automate.yml`)**

```yaml
---
crosscompute: 0.9.2
name: Add Numbers
version: 0.1.0
input:
  variables:
    - id: a
      view: number
      path: variables.dictionary
    - id: b
      view: number
      path: variables.dictionary
output:
  variables:
    - id: c
      view: number
      path: variables.dictionary
batches:
  - name: '{a} + {b}'
    folder: batches/{a}-{b}
    configuration:
      path: datasets/batches.csv
scripts:
  - path: run.py
```
