# CrossCompute Analytics Automation System Documentation

Publish step-by-step wizards that generate web-based reports.

The CrossCompute Analytics Automation System is made of these components:

- [Automation Framework](docs/automation-framework): Transform your Jupyter notebook or command-line script into a step-by-step wizard that generates a web-based report.
- [Editing Platform](docs/editing-platform): Edit your step-by-step wizard and web-based report directly in the browser.
- [Publishing Platform](docs/publishing-platform): Deploy your own step-by-step wizard to generate a custom web-based report for thousands of concurrent users.
- [Analytics Marketplace](docs/analytics-marketplace): Sell subscription access to your step-by-step wizard and web-based report.

To build this documentation, run the following commands:

```bash
# Install dependencies
pip install mkdocs mkdocs-material pygments pymdown-extensions --upgrade

# Launch development server
mkdocs serve

# Build production assets
mkdocs build
```
