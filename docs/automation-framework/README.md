TODO: Add comments to all code

# Automation Framework

Automate your Jupyter notebooks and scripts as web-based reports, tools, widgets, dashboards, wizards.

- Reports are documents that update when the data changes.
- Tools are forms that transform input variables into output variables.
- Widgets are interactive visualizations that update when the data changes.
- Dashboards are widgets in a layout.
- Wizards are step-by-step questions that generate a specific web-based report.

## Quickstart

```bash
# Install package
pip install crosscompute

# Initialize configuration
crosscompute

# Serve analytics
crosscompute serve.yml
```

## Script

CrossCompute will run your script as specified in your configuration file. The script can be a Python script, a Jupyter notebook or a Bash command -- in case your code is in another programming language such as R or Julia.

```yaml
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
script:
  command: >
    python run.py {input_folder} {output_folder} {log_folder} {debug_folder}
```

Here is an example of a simple script that uses command-line arguments and a corresponding configuration file to define a web-based tool.

**Script (`run.py`)**

```python
import json
from os.path import join
from sys import argv


# Get folder paths from command-line arguments
input_folder, output_folder = argv[1:]


# Load input variables from input folder
variables = json.load(open(join(input_folder, 'variables.json'), 'rt'))


# Perform calculation
c = variables['a'] + variables['b']


# Save output variables to output folder
json.dump({
    'c': c,
}, open(join(output_folder, 'variables.json'), 'wt'))
```

**Configuration (`serve.yml`)**

```yaml
---
# version of crosscompute
crosscompute: 0.9.0

# name of your report, tool, widget, dashboard, wizard
name: Add Numbers

# version of your report, tool, widget, dashboard, wizard
version: 0.1.0

# input configuration
input:

  # input variables
  #   - id to use when referencing your variable in the template
  #   - view to use when rendering your variable on the display
  #   - path where your script loads the variable,
  #     relative to the input folder
  variables:
    - id: a
      view: number
      path: variables.json
    - id: b
      view: number
      path: variables.json

# output configuration
output:

  # output variables
  #   - id to use when referencing your variable in the template
  #   - view to use when rendering your variable on the display
  #   - path where your script saves the variable,
  #     relative to the output folder
  variables:
    - id: c
      view: number
      path: variables.json

# test configuration
#   - folder where your test is defined
tests:
  - folder: tests/integers
  - folder: tests/floats

# script configuration
script:

  # folder where your script should run
  folder: .

  # command to use to run your script
  command: python run.py {input_folder} {output_folder}

# display configuration
display:

  # layout to use when rendering your variables
  layout: input output
```

### Environment Variables

CrossCompute will define the following environment variables before running your script:

- ``CROSSCOMPUTE_INPUT_FOLDER``: Your script should expect to find input variables saved to this folder at the relative path specified in the configuration file.
- ``CROSSCOMPUTE_OUTPUT_FOLDER``: Your script should save output variables to this folder at the relative path specified in the configuration file.
- ``CROSSCOMPUTE_LOG_FOLDER``: Your script can save log variables to this folder at the relative path specified in the configuration file. These log variables will be visible to the user.
- ``CROSSCOMPUTE_DEBUG_FOLDER``: Your script can save debug variables to this folder at the relative path specified in the configuration file. These debug variables will not be visible to the user.

Here is an example of a simple script that uses environment variables and a corresponding configuration file to define a web-based tool. Note that you will most likely use environment variables if your script is a Jupyter notebook.

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
variables = json.load(open(join(input_folder, 'variables.json'), 'rt'))


# Perform calculation
c = variables['a'] + variables['b']


# Save output variables to output folder
json.dump({
    'c': c,
}, open(join(output_folder, 'variables.json'), 'wt'))
```

**Configuration (`serve.yml`)**

```yaml
---
# version of crosscompute
crosscompute: 0.9.0

# name of your report, tool, widget, dashboard, wizard
name: Add Numbers

# version of your report, tool, widget, dashboard, wizard
version: 0.1.0

# input configuration
input:

  # input variables
  #   - id to use when referencing this variable in your template
  #   - view to use when rendering this variable on the display
  #   - path where your script loads this variable,
  #     relative to the input folder
  variables:
    - id: a
      view: number
      path: variables.json
    - id: b
      view: number
      path: variables.json

# output configuration
output:

  # output variables
  #   - id to use when referencing this variable in your template
  #   - view to use when rendering this variable on the display
  #   - path where your script saves this variable,
  #     relative to the output folder
  variables:
    - id: c
      view: number
      path: variables.json

# test configuration
#   - folder where your test is defined
tests:
  - folder: tests/integers
  - folder: tests/floats

# script configuration
script:

  # folder where your script should run
  folder: .

  # command to use to run your script
  command: python run.py

# display configuration
display:

  # layout to use when rendering your variables
  layout: input output
```

## Configuration

Configuration files tell CrossCompute how to render your variables and run your script.

```yaml
---
crosscompute: { version of crosscompute }
name: { name of your resource }
version: { version of your resource }
imports:
  - id: { id to use when referencing this import in your template }
    # Specify either path or uri or name
    path: { path to the configuration file that you want to import }
    uri: { uri to the configuration file that you want to import }
    name: { name of the resource that you want to import }
peers:
  - uri: { uri of a trusted peer with which you want to pool resources }
input:
  variables:
    - id: { id to use when referencing this variable in your template }
      view: { view to use when rendering this variable on the display }
      path: { path where your script loads this variable, relative to the
              input folder }
  templates:
    - path: { path to your markdown template or jupyter notebook wizard }
output:
  variables:
    - id: { id to use when referencing this variable in your template }
      view: { view to use when rendering this variable on the display }
      path: { path where your script loads this variable, relative to the
              output folder }
  templates:
    - path: { path to your markdown template or jupyter notebook wizard }
log:
  variables:
    - id: { id to use when referencing this variable in your template }
      view: { view to use when rendering this variable on the display }
      path: { path where your script loads this variable, relative to the
              log folder }
  templates:
    - path: { path to your markdown template or jupyter notebook wizard }
debug:
  variables:
    - id: { id to use when referencing this variable in your template }
      view: { view to use when rendering this variable on the display }
      path: { path where your script loads this variable, relative to the
              debug folder }
  templates:
    - path: { path to your markdown template or jupyter notebook wizard }
tests:
  - folder: { folder that contains an input subfolder with paths for
              input variables that define a specific test }
batches:
  - folder: { folder that contains an input subfolder with paths for
              input variables that define a specific batch }
script:
  folder: { folder where your script should run }
  # Specify either command or function
  command: { command to use to run your script, relative to the script folder }
  function: { function to use to run your script, specified using
              module.function syntax, relative to the script folder }
  schedule: { schedule to use to run your script, specified using extended
              crontab syntax -- second-of-minute minute-of-hour
              hour-of-day day-of-month month-of-year day-of-week }
repository:
  uri: { uri of repository that contains your script }
  folder: { folder that contains this configuration file }
environment:
  variables:
    - id: { id of the environment variable that you want to make available
            to your script }
  image: { image of the container that you want to use to run your script }
  processor: { type of the processor you want to use to run your script,
               either cpu or gpu }
  memory: { amount of memory you want to reserve to run your script }
display:
  style:
    path: { path to CSS stylesheet that will be used to render your templates }
  header:
    path: { path to markdown template that defines the header }
  footer:
    path: { path to markdown template that defines the footer }
  layout: { layout to use by default when rendering this resource,
            either input or output }
  format: { format to use by default when rendering this resource }
payment:
  account: { account where the user should send payment when using this
             resource }
  amount: { amount of payment that the user should send }
  currency: { currency of payment }
  policy: { policy to use for payment, either before or after }
```

## Examples

For more examples, please see <https://github.com/crosscompute/crosscompute-examples>.

### Report

Here is an example of a report configuration. See <https://github.com/crosscompute/crosscompute-examples/tree/0.9/reports/compute-logarithms> for the complete example.

**Configuration (`serve.yml`)**

```yaml
---
crosscompute: 0.9.0
name: Compute Logarithms
version: 0.0.1
input:
  variables:
    - id: base
      view: number
      path: variables.json
    - id: start
      view: number
      path: variables.json
    - id: stop
      view: number
      path: variables.json
    - id: step
      view: number
      path: variables.json
output:
  variables:
    - id: logarithms
      view: table
      path: values.csv
  templates:
    - path: report.md
tests:
  - folder: tests/base-e
  - folder: tests/base-10
batches:
  - folder: batches/base-2
  - folder: batches/base-e
  - folder: batches/base-10
script:
  folder: .
  command: python -c "$(jupyter nbconvert run.ipynb --to script --stdout)"
repository:
  uri: https://github.com/crosscompute/crosscompute-examples
  folder: reports/compute-logarithms
environment:
  image: docker.io/library/python:slim-buster
  processor: cpu
  memory: tiny
display:
  style:
    path: report.css
  header:
    path: header.md
  footer:
    path: footer.md
  layout: output
  format: pdf
```

**Template (`report.md`)**

```markdown
# Logarithm Table: Base { base }

{ logarithms }
```

TODO: Screenshot

### Tool

Here is an example of a tool configuration. See <https://github.com/crosscompute/crosscompute-examples/tree/0.9/tools/add-numbers-command-line> for the complete example.

**Configuration (`serve.yml`)**

```yaml
---
# version of crosscompute
crosscompute: 0.9.0

# name of your report, tool, widget, dashboard, wizard
name: Add Numbers

# version of your report, tool, widget, dashboard, wizard
version: 0.1.0

# input configuration
input:

  # input variables
  #   - id to use when referencing this variable in your template
  #   - view to use when rendering this variable on the display
  #   - path where your script loads this variable,
  #     relative to the input folder
  variables:
    - id: a
      view: number
      path: variables.json
    - id: b
      view: number
      path: variables.json

# output configuration
output:

  # output variables
  #   - id to use when referencing this variable in your template
  #   - view to use when rendering this variable on the display
  #   - path where your script saves this variable,
  #     relative to the output folder
  variables:
    - id: c
      view: number
      path: variables.json

# test configuration
#   - folder where your test is defined
tests:
  - folder: tests/integers
  - folder: tests/floats

# script configuration
script:

  # folder where your script should run
  folder: .

  # command to use to run your script
  command: python run.py

# display configuration
display:

  # layout to use when rendering your variables
  layout: input output
```

TODO: Screenshot

### Widget

Here is an example of a widget configuration. See <https://github.com/crosscompute/crosscompute-examples/tree/0.9/widgets/watch-cpu> for the complete example.

**Configuration (`serve.yml`)**

```yaml
---
crosscompute: 0.9.0
name: Watch CPU Usage
version: 0.0.1
output:
  variables:
    - id: cpu-usage
      view: number
      path: variables.json
tests:
  - folder: tests/standard
script:
  folder: .
  function: run.plot
  schedule: '* * * * * *'
display:
  layout: output
```

TODO: Screenshot

### Dashboard

Here is an example of a dashboard configuration. See <https://github.com/crosscompute/crosscompute-examples/tree/0.9/dashboards/watch-machine> for the complete example.

**Configuration (`serve.yml`)**

```yaml
---
crosscompute: 0.9.0
name: Watch Machine
version: 0.0.1
imports:
  - id: cpu
    path: ../../widgets/watch-cpu/serve.yml
  - id: ram
    path: ../../widgets/watch-ram/serve.yml
output:
  templates:
    - path: dashboard.md
display:
  layout: output
```

**Template (`dashboard.md`)**

```markdown
# CPU
{ cpu }

# RAM
{ ram }
```

TODO: Screenshot

### Wizard

Here is an example of a wizard configuration. See <https://github.com/crosscompute/crosscompute-examples/tree/0.9/wizards/encourage-exercise> for the complete example.

**Configuration (`serve.yml`)**

```yaml
---
crosscompute: 0.9.0
name: Encourage Exercise
version: 0.0.1
input:
  variables:
    - id: more_exercise
      view: boolean
      path: variables.json
    - id: simple_exercise
      view: string
      path: variables.json
  templates:
    - path: ask.ipynb
output:
  variables:
    - id: summary
      view: markdown
      path: summary.md
tests:
  - folder: tests/standard
script:
  folder: .
  command: python -c "$(jupyter nbconvert run.ipynb --to script --stdout)"
display:
  layout: output
```

**Template (`ask.ipynb`)**

```markdown
Would you like to exercise more?
- Yes
- No

{more_exercise}
```

```python
def show_next(more_exercise):
	if more_exercise == 'Yes':
		return True
```

```markdown
Name a simple exercise you can do right now and do it.

{simple_exercise}
```

```python
def check(simple_exercise):
	if simple_exercise.strip() == '':
        return False, {'simple_exercise': 'cannot be blank'}
```

## Plugins

TODO: Add instructions on how to make a view plugin
