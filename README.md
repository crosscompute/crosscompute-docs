# CrossCompute Analytics Automation System Documentation

Webify your scripts.

- [Automation Framework](docs/automation-framework): Webify your Jupyter notebook or command-line script into a form that generates a report.
- [Editing Extension](docs/editing-extension): Prototype your analytics collaboratively in JupyterLab with our CrossCompute extensions.
- [Analytics Marketplace](docs/analytics-marketplace): Sell subscription access to your reusable report.

To build this documentation, run the following commands:

```bash
# Install dependencies
pip install --upgrade \
    mkdocs \
    mkdocs-material \
    pre-commit \
    pygments \
    pymdown-extensions

# Install pre-commit hooks
pre-commit install

# Launch development server
mkdocs serve

# Build production assets
mkdocs build
```
