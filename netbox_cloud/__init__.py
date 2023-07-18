

import sys
import os

# Set the base directory two levels up
CLOUD_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Open setup.py file
setup_file = open(f"{CLOUD_BASE_DIR}/env.py", 'r')

# Read the contents of the file
setup_content = setup_file.read()

# Close the file
setup_file.close()


import json

get_var = setup_content.replace("CONFIG_VARIABLES = ", "")
parameters = json.loads(get_var)

# Netbox plugin related import
from extras.plugins import PluginConfig

class CloudConfig(PluginConfig):
    name = parameters.get("plugin_name")
    verbose_name = parameters.get("verbose_name")
    description = parameters.get("description")
    version = parameters.get("version")
    author = parameters.get("author_name")
    author_email = parameters.get("author_email")
    base_url = "cloud"
    required_settings = []
    default_settings = {}
    #django_apps = ['netbox_proxbox']

config = CloudConfig