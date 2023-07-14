# Netbox plugin related import
from extras.plugins import PluginConfig

class CloudConfig(PluginConfig):
    name = "netbox_cloud"
    verbose_name = "NetBox Cloud"
    description = "Making NetBox support Cloud environments"
    version = "0.0.1"
    author = "Emerson Felipe (@emersonfelipesp)"
    author_email = "emerson@netdevopsbr.com"
    base_url = "cloud"
    required_settings = []
    default_settings = {}
    #django_apps = ['netbox_proxbox']

config = CloudConfig