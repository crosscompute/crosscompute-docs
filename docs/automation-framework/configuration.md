Configuration files tell CrossCompute how to render your variables and run your script.

### Current

Here are the options supported in the current release:

```yaml
---
# Examples: https://github.com/crosscompute/crosscompute-examples
# Documentation: https://d.crosscompute.com
# Forum: https://forum.crosscompute.com

# version of crosscompute
crosscompute: 0.0.0

# name of your automation
name: Automation X

# slug for automation URI
slug: automation-x

# version of your automation
version: 0.0.0

# imports configuration
# - id to use when referencing this import in your template
# - path to the configuration file that you want to import
imports:
  - id: automation-y
    path: tools/automation-y/automate.yml

# input configuration
input:

  # input variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script loads the variable, relative to the input folder;
  #   specify ENVIRONMENT to prevent saving the variable to disk
  # - configuration of the view
  variables:
    - id: x1
      view: string
      path: variables.dictionary
    - id: x2
      view: number
      path: variables.dictionary
    - id: x3
      view: password
      path: ENVIRONMENT
    - id: x4
      view: email
      path: ENVIRONMENT
    - id: x5
      view: text
      path: x5.txt
    - id: x6
      view: markdown
      path: x6.md

  # input templates
  # - path to your markdown template or jupyter notebook form
  templates:
    - path: form.md

# output configuration
# output:

  # output variables
  # - id to use when referencing your variable in the template
  # - view to use when rendering your variable on the display
  # - path where your script saves the variable,
  #   relative to the output folder
  # - configuration of the view
  variables:
    - id: y1
      view: link
      path: y1.pdf
    - id: y2
      view: string
      path: variables.dictionary
    - id: y3
      view: number
      path: variables.dictionary
    - id: y4
      view: text
      path: y4.txt
    - id: y5
      view: markdown
      path: y5.md
    - id: y6
      view: image
      path: y6.svg
    - id: y7
      view: table
      path: y7.json
    - id: y8
      view: map-mapbox
      path: y8.geojson
      configuration:
        style: mapbox://styles/mapbox/dark-v10
        layers:
          - type: fill
            type: circle
            paint:
              fill-color: blue
              circle-color: red
        path: y8-configuration.json
    - id: y9
      view: map-deck-screengrid
      path: y9.json
      configuration:
        style: mapbox://styles/mapbox/dark-v10
        path: y9-configuration.json

  # output templates
  # - path to your markdown template or jupyter notebook form
  templates:
    - path: report-section1.md
    - path: report-section2.md

# tests configuration
# - folder that contains an input subfolder with paths for
#   input variables that define a specific test
tests:
  - folder: tests/test1
  - folder: tests/test2

# batches configuration
# - name of the batch; can include variable ids and filters
# - slug for batch URI; can include variable ids and filters
# - folder that contains an input subfolder with paths for
#   input variables; can include variable ids and filters
# - reference batch to use to fill omitted variables in batch configuration
# - configuration for batch template
batches:

  # case 0: use a batch folder to set values for input variables
  - folder: batches/batch0

  # case 1: use a batch configuration to vary values for input variables
  - name: '{x1 | title} {x2}'
    slug: '{x1 | slug}-{x2}'
    folder: batches/{x1 | slug}-{x2}
    configuration:
      path: datasets/batches.csv

  # case 2: use a reference folder to set default values for missing variables
  #         use a batch configuration to vary selected variables
  - name: '{x1 | title} {x2}'
    slug: '{x1 | slug}-{x2}'
    folder: batches/{x1 | slug}-{x2}
    reference:
      folder: batches/batch0
    configuration:
      path: datasets/batches.csv

# scripts configuration
# - path to your script, relative to the script folder
# - command to run your script, if path is not specified
# - folder where your script should run
scripts:
  - path: run1.ipynb
    command: python run1.py {input_folder} {output_folder} {log_folder} {debug_folder}
    folder: .
  - path: run2.ipynb
    command: python run2.py {input_folder} {output_folder} {log_folder} {debug_folder}
    folder: .

# display configuration
display:

  # styles configuration
  # - uri to CSS stylesheet that will be used to render your templates
  # - path to CSS stylesheet that will be used to render your templates
  styles:
    - uri: https://fonts.googleapis.com/css?family=Tangerine
    - path: report.css

  # templates configuration
  # - id of template
  # - path to template
  templates:
    - id: root
      path: root.jinja2
```

### Future

Here is the complete specification, including options that are not yet implemented in the current release.

```yaml
---
crosscompute: { version of crosscompute }
name: { name of your automation }
version: { version of your automation }
imports:
  - id: { id to use when referencing this import in your template }
    visibility: { visibility level -- home or index or search }
    # Specify either path or folder or uri or name
    path: { path to the configuration file that you want to import }
    uri: { uri to the configuration file that you want to import }
    name: { name of the automation that you want to import }
peers:
  - uri: { uri of a trusted peer for imports and exports }
input:
  variables:
    - id: { id to use when referencing this variable in your template }
      view: { view to use when rendering this variable on the display }
      path: { path where your script loads this variable, relative to the
              input folder }
      configuration: { configuration of the view }
  templates:
    - path: { path to your markdown template or jupyter notebook form }
output:
  variables:
    - id: { id to use when referencing this variable in your template }
      view: { view to use when rendering this variable on the display }
      path: { path where your script loads this variable, relative to the
              output folder }
      configuration: { configuration of the view }
  templates:
    - path: { path to your markdown template or jupyter notebook form }
log:
  variables:
    - id: { id to use when referencing this variable in your template }
      view: { view to use when rendering this variable on the display }
      path: { path where your script loads this variable, relative to the
              log folder }
      configuration: { configuration of the view }
  templates:
    - path: { path to your markdown template or jupyter notebook form }
debug:
  variables:
    - id: { id to use when referencing this variable in your template }
      view: { view to use when rendering this variable on the display }
      path: { path where your script loads this variable, relative to the
              debug folder }
      configuration: { configuration of the view }
  templates:
    - path: { path to your markdown template or jupyter notebook form }
views:
    - id: { id of the view that you want to configure }
      configuration: { configuration of the view }
      folder: { folder containing the view class }
      # Specify either package or uri or class
      package: { package containing the view on PyPI }
      uri: { uri containing the view remotely }
      class: { class containing the view locally, specified using
               module.class syntax, relative to the view folder }
tests:
  - folder: { folder that contains an input subfolder with paths for
              input variables that define a specific test }
batches:
  - name: { name of the batch; can include variable ids and filters }
    slug: { slug for batch URI; can include variable ids and filters }
    folder: { folder that contains an input subfolder with paths to
              input variables; can include variable ids and filters }
    reference:
      folder: { folder that contains an input subfolder to use as a reference
                for omitted variables }
    variables:
      - id: { id of a variable that you want to vary }
        code: { code to generate values for this variable }
    configuration:
      path: { path containing different values for the input variables }
datasets:
  - path: { path to your dataset }
    reference:
      path: { path to reference dataset if expected path does not exist }
setups:
  - folder: { folder where your setup should run }
    dependencies:
      - package: { package on PyPI }
    command: { command to use to setup your script, relative to the setup folder }
scripts:
  - path: { path to your script, relative to the script folder }
    command: { command to run your script, if path is not specified }
    function: { function to use to run your script, if path or command is not
                specified }
    folder: { folder where your script should run }
    schedule: { schedule to use to run your script, specified using extended
                crontab syntax -- second-of-minute minute-of-hour
                hour-of-day day-of-month month-of-year day-of-week }
repository:
  uri: { uri of repository that contains your script }
  folder: { folder that contains this configuration file }
environment:
  variables:
    - id: { id of the environment variable to make available to your script }
  image: { image of the container that you want to use to run your script }
  processor: { type of the processor you want to use to run your script,
               either cpu or gpu }
  memory: { amount of memory you want to reserve to run your script }
display:
  styles:
    - uri: { uri to CSS stylesheet that will style your templates }
    - path: { path to CSS stylesheet that will style your templates }
  templates:
    - id: { id of your template }
      path: { path to your template }
  layout: { layout to use when no templates are defined }
  format: { format to use when rendering this automation }
payment:
  account: { account where the user should send payment when using this
             automation }
  amount: { amount of payment that the user should send }
  currency: { currency of payment }
  policy: { policy to use for payment, either before or after }
```
