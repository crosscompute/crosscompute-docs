Configuration files tell CrossCompute how to render your variables and run your script.

### Current

Here are the options supported in the current release:

```yaml
---
crosscompute: 0.9.1
name: { name of your automation }
slug: { slug for automation URI }
version: { version of your automation }
imports:
  - id: { id to use when referencing this import in your template }
    path: { path to the configuration file that you want to import }
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
    configuration:
      path: { path containing different values for the input variables }
scripts:
  - path: { path to your script, relative to the script folder }
    command: { command to run your script, if path is not specified }
    folder: { folder where your script should run }
display:
  styles:
    - uri: { uri to CSS stylesheet that will style your templates }
    - path: { path to CSS stylesheet that will style your templates }
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
