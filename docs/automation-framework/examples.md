For more examples, please see <https://github.com/crosscompute/crosscompute-examples>.

### Report

A report is a document that updates when the data changes.

Here is an example of a report configuration. See <https://github.com/crosscompute/crosscompute-examples/tree/master/reports/compute-logarithms> for the complete example.

**Configuration (`automate.yml`)**

```yaml
---
# version of crosscompute
crosscompute: 0.9.2

# name of your automation
name: Compute Logarithms

# version of your automation
version: 0.0.1

# input configuration
input:

  # input variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script loads the variable,
  #   relative to the input folder
  variables:
    - id: base
      view: number
      path: variables.dictionary
    - id: start
      view: number
      path: variables.dictionary
    - id: stop
      view: number
      path: variables.dictionary
    - id: step
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
    - id: logarithms
      view: table
      path: values.csv

  # output templates
  # - path to your markdown template or jupyter notebook form
  templates:
    - path: report.md

# tests configuration
# - folder that contains an input subfolder with paths for
#   input variables that define a specific test
tests:
  - folder: tests/base-e
  - folder: tests/base-10

# batches configuration
# - folder that contains an input subfolder with paths for
#   input variables that define a specific batch
batches:
  - folder: batches/base-2
  - folder: batches/base-e
  - folder: batches/base-10

# scripts configuration
# - path to your script, relative to the script folder
# - folder where your script should run
scripts:
  - path: run.ipynb
    folder: .

# repository configuration
repository:

  # uri of repository that contains your script
  uri: https://github.com/crosscompute/crosscompute-examples

  # folder that contains this configuration file
  folder: reports/compute-logarithms

# environment configuration
environment:

  # image of the container that you want to use to run your script
  image: docker.io/library/python:slim-buster

  # type of the processor you want to use to run your script, either
  # cpu or gpu
  processor: cpu

  # amount of memory you want to reserve to run your script
  memory: tiny

# display configuration
display:

  # styles configuration
  # - uri to CSS stylesheet that will be used to render your templates
  # - path to CSS stylesheet that will be used to render your templates
  styles:
    - path: report.css
```

**Template (`report.md`)**

```markdown
# Logarithm Table: Base { base }

{ logarithms }
```

TODO: Screenshot

### Tool

A tool is a form with code that transforms input variables into output variables.

Here is an example of a tool configuration. See <https://github.com/crosscompute/crosscompute-examples/tree/master/tools/add-numbers> for the complete example.

**Configuration (`automate.yml`)**

```yaml
---
# version of crosscompute
crosscompute: 0.9.2

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

# scripts configuration
# - command to use to run your script
# - folder where your script should run
scripts:
  - command: python run.py {input_folder} {output_folder}
    folder: .
```

TODO: Screenshot

### Widget

A widget is an interactive visualization that updates when the data changes.

Here is an example of a widget configuration. See <https://github.com/crosscompute/crosscompute-examples/tree/master/widgets/watch-cpu> for the complete example.

**Configuration (`automate.yml`)**

```yaml
---
# version of crosscompute
crosscompute: 0.9.2

# name of your automation
name: Watch CPU Usage

# version of your automation
version: 0.0.1

# output configuration
output:

  # output variables
  #   - id to use when referencing your variable in the template
  #   - view to use when rendering your variable on the display
  #   - path where your script saves the variable,
  #     relative to the output folder
  variables:
    - id: cpu-usage
      view: number
      path: variables.dictionary

# tests configuration
#   - folder that contains an input subfolder with paths for
#     input variables that define a specific test
tests:
  - folder: tests/standard

# scripts configuration
# - path to your script, relative to the script folder
# - command to use to run your script, if path is not specified
# - function to use to run your script, if path or command is not specified
# - folder where your script should run
# - schedule to use to run your script, specified using extended crontab syntax
scripts:
  - function: run.plot
    folder: .
    schedule: '* * * * * *'
```

TODO: Screenshot

### Dashboard

A dashboard is a collection of widgets.

Here is an example of a dashboard configuration. See <https://github.com/crosscompute/crosscompute-examples/tree/master/dashboards/watch-machine> for the complete example.

**Configuration (`automate.yml`)**

```yaml
---
# version of crosscompute
crosscompute: 0.9.2

# name of your automation
name: Watch Machine

# version of your automation
version: 0.0.1

# import configuration
# - id to use when referencing this import in your template
# - path to the configuration file that you want to import
imports:
  - id: cpu
    path: ../../widgets/watch-cpu/automate.yml
  - id: ram
    path: ../../widgets/watch-ram/automate.yml

# output configuration
output:

  # output templates
  # - path to your markdown template or jupyter notebook form
  templates:
    - path: dashboard.md
```

**Template (`dashboard.md`)**

```markdown
# CPU
{ cpu }

# RAM
{ ram }
```

TODO: Screenshot

### Form

A form is a step-by-step series of questions.

Here is an example of a form configuration. See <https://github.com/crosscompute/crosscompute-examples/tree/master/forms/encourage-exercise> for the complete example.

**Configuration (`automate.yml`)**

```yaml
---
# version of crosscompute
crosscompute: 0.9.2

# name of your automation
name: Encourage Exercise

# version of your automation
version: 0.0.1

# input configuration
input:

  # input variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script loads the variable,
  #   relative to the input folder
  variables:
    - id: more_exercise
      view: boolean
      path: variables.dictionary
    - id: simple_exercise
      view: string
      path: variables.dictionary

  # input templates
  # - path to your markdown template or jupyter notebook form
  templates:
    - path: ask.ipynb

# output configuration
output:

  # output variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script saves the variable,
  #   relative to the output folder
  variables:
    - id: summary
      view: markdown
      path: summary.md

# tests configuration
# - folder that contains an input subfolder with paths for
#   input variables that define a specific test
tests:
  - folder: tests/standard

# scripts configuration
# - path to your script, relative to the script folder
# - folder where your script should run
scripts:
  - path: run.ipynb
    folder: .
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
    'Decide whether to show the next step'
    if more_exercise == 'Yes':
        return True
```

```markdown
Name a simple exercise you can do right now and do it.

{simple_exercise}
```

```python
def check(simple_exercise):
    'Check values from previous steps'
    if simple_exercise.strip() == '':
        return False, {'simple_exercise': 'cannot be blank'}
```
