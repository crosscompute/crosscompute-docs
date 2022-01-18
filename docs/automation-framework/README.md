# Automation Framework

Automate your Jupyter notebooks and scripts as web-based reports, tools, widgets, dashboards, forms. CrossCompute is designed to be decoupled, meaning that your notebook or script should know as little about CrossCompute as possible. All of the information that CrossCompute needs to know to run your script and render your variables is in a configuration file.

## Quickstart

You can use our self-contained server to prototype automations on your local machine. Note that the package requires Python 3.9.

```bash
# Prepare environment
sudo dnf -y install python3.9
# sudo apt -y install python3.9
python3.9 -m venv ~/.virtualenvs/crosscompute
source ~/.virtualenvs/crosscompute/bin/activate

# Update package
pip install crosscompute>=0.9.1 crosscompute-views-map>=0.0.2 --upgrade

# Initialize configuration
crosscompute

# Serve automation
crosscompute automate.yml
```

Running `crosscompute` without any arguments will start a server if a configuration file exists. If a configuration does not exist, `crosscompute` will ask questions to initialize a configuration file.
