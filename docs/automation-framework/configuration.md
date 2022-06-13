Configuration files tell CrossCompute how to render your variables and run your script.

### Current

Here are the options supported in the current release:

```yaml
---
# Reference: https://github.com/crosscompute/crosscompute-examples
# Gallery: https://crosscompute.net
# Documentation: https://docs.crosscompute.com
# Forum: https://forum.crosscompute.com

# version of crosscompute (required)
crosscompute: 0.9.2

# name of your automation
name: Automation X

# slug for automation URI
# slug: automation-x

# version of your automation
version: 0.0.0

# imports configuration
# - path to the configuration file that you want to import (required)
# - id to use when referencing this import in your template
imports:
  - path: tools/automation-y/automate.yml
    id: automation-y

# input configuration
input:

  # input variables
  # - id to use when referencing your variable in the template (required)
  # - view to use when rendering your variable on the display (required)
  # - path where your script loads the variable, relative to the input folder;
  #   specify ENVIRONMENT to prevent saving the variable to disk (required)
  # - configuration of the view
  variables:
    - id: x1
      view: string
      path: variables.dictionary
    - id: x2
      view: number
      path: variables.dictionary
      configuration:
        label: YOUR-LABEL-TEXT
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
  # - path to your markdown template or jupyter notebook form (required)
  templates:
    - path: form1.md
    - path: form2.md

# output configuration
output:

  # output variables
  # - id to use when referencing your variable in the template (required)
  # - view to use when rendering your variable on the display (required)
  # - path where your script saves the variable, relative to the output
  #   folder (required)
  # - configuration of the view
  variables:
    - id: y1
      view: link
      path: y1.pdf
      configuration:
        link-text: YOUR-LINK-TEXT
        file-name: YOUR-FILE-NAME
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
  # - path to your markdown template or jupyter notebook form (required)
  templates:
    - path: report-section1.md
    - path: report-section2.md

# batches configuration
# - folder that contains an input subfolder with paths for
#   input variables; can include variable ids and filters (required)
# - name of the batch; can include variable ids and filters
# - slug for batch URI; can include variable ids and filters
# - reference batch to use to fill omitted variables in batch configuration
# - configuration for batch template
batches:

  # case 0: use a batch folder to set values for input variables
  - folder: batches/standard

  # case 1: use a batch configuration to vary values for input variables
  - folder: batches/{x1 | slug}-{x2}
    name: '{x1 | title} {x2}'
    slug: '{x1 | slug}-{x2}'
    configuration:
      path: datasets/batches.csv

  # case 2: use a reference folder to set default values for missing variables
  #         use a batch configuration to vary selected variables
  - folder: batches/{x1 | slug}-{x2}
    name: '{x1 | title} {x2}'
    slug: '{x1 | slug}-{x2}'
    reference:
      folder: batches/standard
    configuration:
      path: datasets/batches.csv

# datasets configuration
# - path of a dataset expected by your script
# - reference dataset if expected path does not exist
datasets:
  - path: datasets/abc.csv
    reference:
      path: datasets/abc-2022.csv

# scripts configuration
# - path to your script, relative to the script folder
# - command to run your script, if path is not specified
# - folder where your script should run
scripts:
  - path: run.ipynb
    command: python run.py {input_folder} {output_folder} {log_folder} {debug_folder}
    folder: .
  - path: run2.ipynb
    command: python run2.py {input_folder} {output_folder} {log_folder} {debug_folder}
    folder: .

# environment configuration
environment:

  # environment variables
  # - id of the environment variable to make available to your script (required)
  variables:
    - id: GOOGLE_KEY

  # batch concurrency, either process, thread or single
  batch: process

  # interval to wait before running your scripts again
  interval: 30 minutes

# display configuration
display:

  # styles configuration
  # - path to CSS stylesheet that will be used to render your templates
  # - uri to CSS stylesheet that will be used to render your templates
  styles:
    - path: report.css
    - uri: https://fonts.googleapis.com/css?family=Tangerine

  # templates configuration
  # - path to template (required)
  # - id of template
  templates:
    - path: base.jinja2
      id: base
    - path: live.jinja2
      id: live
    - path: root.jinja2
      id: root

  # pages configuration
  # - id of the page (required)
  # - configuration of the page
  pages:
    - id: automation
      configuration:
        design: input
        design: output
        design: none
    - id: input
      configuration:
        design: flex-vertical
    - id: output
      configuration:
        design: none

# authorization configuration
authorization:
  tokens:
    - path: tokens.yml
  groups:
    - configuration:
        role_name: admin
      permissions:
        - id: add_authorization
        - id: see_automation
        - id: see_batch
        - id: run_automation
    - configuration:
        role_name:
          - leader
          - member
      permissions:
        - id: see_automation
        - id: see_batch
          action: match

# prints configuration
prints:
  - format: pdf
    configuration:
      header-footer:
        font-family: sans-serif
        font-size: 8pt
        color: '#808080'
        padding: 0.1in 0.25in
        skip-first: true
      page-number:
        location: footer
        alignment: right
    folder: ~/Documents/attachments/automation-x-{timestamp}
    name: '{y2 | slug}-{y3}.pdf'
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
scripts:
  - path: { path to your script, relative to the script folder }
    command: { command to run your script, if path is not specified }
    function: { function to use to run your script, if path or command is not
                specified }
    folder: { folder where your script should run }
repository:
  uri: { uri of repository that contains your script }
  folder: { folder that contains this configuration file }
environment:
  variables:
    - id: { id of the environment variable to make available to your script }
  interval: { interval to wait before running your scripts again }
  container:
    image: { image of the container that you want to use to run your script }
    packages:
      - id: { id of the package that you want installed }
        manager: { manager that you want to use to install the package }
        repository: { repository of packages e.g. rpmfusion-free }
  processor: { processor type you want to use to run your script,
               either cpu or gpu }
  memory: { memory amount you want to reserve to run your script }
  batch: { batch concurrency, either process, thread or single }
display:
  styles:
    - uri: { uri to CSS stylesheet that will style your templates }
    - path: { path to CSS stylesheet that will style your templates }
  templates:
    - id: { id of your template }
      path: { path to your template }
  pages:
    - id: { id of the page }
      configuration:
        design: { design of the page }
authorization:
  tokens:
    - path: { path to static tokens }
  groups:
    - configuration: { configuration of group as defined by token variables }
      permissions:
        - id: { add_authorization, see_automation, see_batch, run_automation }
          action: { accept, match }
prints:
  - format: { format to use when printing this automation }
    configuration:
      header-footer: { header footer settings }
      page-number: { page number settings }
    templates:
      - id: { id of your template }
        path: { path to your template }
    folder: { folder to use when printing this automation }
    name: { name to use when printing this automation }
markets:
  - uri: { uri of a trusted market }
payment:
  account: { account where the user should send subscription payment
             e.g. nano address }
  period: { period of subscription e.g. month }
  amount: { amount of payment that the user should send }
  currency: { currency of payment e.g. nano }
```
