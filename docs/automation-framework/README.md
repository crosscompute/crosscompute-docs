# Automation Framework

Webify your Jupyter notebook or command-line script into a form that generates a report. CrossCompute is designed to be decoupled, meaning that your notebook or script should know as little about CrossCompute as possible. Most of the information that CrossCompute needs to know to run and render your variables is in a configuration file.

## Quickstart

You can use our self-contained server to prototype automations on your local machine. Note that the package requires at least Python 3.9.

```bash
# Prepare environment
sudo dnf -y install python3.9
python3.9 -m venv ~/.virtualenvs/crosscompute
source ~/.virtualenvs/crosscompute/bin/activate

# Update package
pip install \
    crosscompute>=0.9.2 \
    crosscompute-views-map>=0.0.2

# Initialize configuration
crosscompute

# Serve automation
crosscompute automate.yml
```

Running `crosscompute` without any arguments will start a server if a configuration file exists. If a configuration does not exist, `crosscompute` will ask questions to initialize a configuration file.
