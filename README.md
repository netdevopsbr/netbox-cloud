# netbox-cloud
Cloud solution inside NetBox (initially with Proxmox and Vmware integration)

---

I plan to manage to make the plugin able to manage on-premises (private) clouds and hybrid clouds.
**NOTE:** I discussed this with some people that thought it was not the core idea of NetBox, but I disagree and going to do this anyway as I'm already doing with Proxbox plugin.

The **NetBox Cloud** plugin will also **integrate with Proxmox hypervisor** using the **[netbox-proxbox](https://github.com/netdevopsbr/netbox-proxbox)**, but the idea is to have a much more comprehensive integration with other on-premises solutions and public clouds.

---

## Roadmap
- Create plugin base code
- Create **specific Django models to represent Cloud environment**, like VMs, Containers, **Networks**,** Firewalls**, etc...
- Integrate with **Proxmox** (netbox-proxbox plugin)
- Integrate with **Vmware** (I'm going to check if there's ongoing work with NetBox or if I need to kick off from bootstrap)
- Deploy **long-term version**
- Integrate with **DigitalOcean**
- Integrate with **AWS** and **Azure** (I need external help)
