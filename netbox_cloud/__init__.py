# Netbox plugin related import
from extras.plugins import PluginConfig

from netbox_cloud import env

class CloudConfig(PluginConfig):
    name = env.name
    verbose_name = env.verbose_name
    description = env.description
    version = env.version
    author = env.author_name
    author_email = env.author_email
    base_url = "cloud"
    required_settings = []
    default_settings = {}
    #django_apps = ['netbox_proxbox']

config = CloudConfig