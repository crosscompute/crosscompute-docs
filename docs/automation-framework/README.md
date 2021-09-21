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

CrossCompute will run your script as specified in your configuration file. The script can be a Python script, a Jupyter notebook or a Bash command -- in case your code is in another programming language such as R or Julia. CrossCompute will define the following environment variables before running your script:

- ``CROSSCOMPUTE_INPUT_FOLDER``: Your script should expect to find input variables saved to this folder at the relative path specified in the configuration file.
- ``CROSSCOMPUTE_OUTPUT_FOLDER``: Your script should save output variables to this folder at the relative path specified in the configuration file.
- ``CROSSCOMPUTE_LOG_FOLDER``: Your script can save log variables to this folder at the relative path specified in the configuration file. These log variables will be visible to the user.
- ``CROSSCOMPUTE_DEBUG_FOLDER``: Your script can save debug variables to this folder at the relative path specified in the configuration file. These debug variables will not be visible to the user.

Here is an example of a simple script that adds two numbers, the corresponding configuration file and resulting web-based tool.

**Script (```run.py```)**

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

**Configuration (```serve.yml```)**

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
#   - folder where test is defined
tests:
  - folder: tests/integers
  - folder: tests/floats

# script configuration
script:

  # folder where script should run
  folder: .

  # command to use to run your script
  command: python run.py

# display configuration
display:

  # layout to use when rendering your variables
  layout: input output
```

**Tool**

TODO: Screenshot

TODO: Add links to crosscompute-examples github

## Configuration

Configuration files tell CrossCompute how to render your variables and run your script.

```yaml
---
crosscompute: { version of crosscompute }
name: { name of your report, tool, widget, dashboard, wizard }
version: { version of your report, tool, widget, dashboard, wizard }
# imports:
#   - id: {}
#     path: {}
#     uri: {}
#     name: {}
#     version: {}
# peers:
#   - uri: {}
input:
  variables:
    - id: {}
      view: {}
      path: {}
# templates:
#   - path: {}
output:
  variables:
    - id: {}
      view: {}
      path: {}
# templates:
#   - path: {}
tests:
  - folder: tests/standard
# batches:
#   - folder: {}
script:
  folder: {}
  command: {}
  function: {}
  schedule: {}
# repository:
#   uri: {}
#   folder: {}
# environment:
#   image:
#   processor:
#   memory:
display:
  style: {}
  header:
    path: {}
  footer:
    path: {}
  layout: {}
  format: {}
```

## Examples

For more examples, please see <https://github.com/crosscompute/crosscompute-examples>.

### Report

Here is an example of a report configuration:

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
  style: report.css
  header:
    path: header.md
  footer:
    path: footer.md
  layout: output
  format: pdf
```

TODO: Add example of markdown template

### Tool

Here is an example of a tool configuration:

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
#   - folder where test is defined
tests:
  - folder: tests/integers
  - folder: tests/floats

# script configuration
script:

  # folder where script should run
  folder: .

  # command to use to run your script
  command: python run.py

# display configuration
display:

  # layout to use when rendering your variables
  layout: input output
```

### Widget

Here is an example of a widget configuration:

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
  schedule: '* * * * * * *'
display:
  layout: output
```

### Dashboard

Here is an example of a dashboard configuration:

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

TODO: Add example of markdown template

### Wizard

Here is an example of a wizard configuration:

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

TODO: Add example or screenshot of ipynb template

## Plugins

TODO: Add instructions on how to make a view plugin
