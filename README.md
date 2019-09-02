# add_vlans
Searches for all active VLANs, and then creates the missing VLANs on the other targets

Performs a lookup of the VLAN database, to write the information as a usable YAML file that can then be used to create all missing (active) VLANs on edge switches where they are missing.

Uses a python script to clean up the variables file.

First run the show_vlans.yml playbook to fetch all vlan data, then run the add_vlan to configure the vlans.
Alternatively, the add_vlan can be added as a role, to automate the whole process.
