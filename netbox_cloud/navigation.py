from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices

proxmox_item = PluginMenuItem(
    link='plugins:netbox_cloud:containers',
    link_text='Containers',
)

vmware_item = PluginMenuItem(
    link='plugins:netbox_cloud:containers',
    link_text='Containers',
)

menu = PluginMenu(
    label='Cloud',
    groups=(
        ('Proxmox', (proxmox_item,)),
        ('Vmware', (vmware_item,)),
    ),
    icon_class='mdi mdi-cloud'
)

