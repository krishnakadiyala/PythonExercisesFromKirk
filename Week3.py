"""
Part 3 - Exercise 1:
vlan_list = []

with open("show_vlan.txt") as f:
    show_vlan = f.read()

for line in show_vlan.splitlines():
    if "VLAN" in line or "-----" in line or line.startswith(" "):
        continue
    fields = line.split()
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_list.append((vlan_id, vlan_name))
   
print()
print(vlan_list)
Exercise2:
with open("show_arp.txt") as f:
    show_arp = f.read()

print()
found1 = False
found2 = False

for line in show_arp.splitlines():
    if "protocol" in line.lower():
        continue
    fields = line.split()
    ip_addr = fields[1]
    mac_addr = fields[3]
    if ip_addr == "10.220.88.1":
        print("Default gateway IP/Mac is: {}/{}".format(ip_addr,mac_addr))
        found1 = True
    elif ip_addr == "10.220.88.30":
        print("Arista IP/Mac is: {}/{}".format(ip_addr,mac_addr))
        found2 = True

    if found1 and found2:
        print("Done.")
        break

Exercise 3:

with open("show_lldp.txt") as f:
    show_lldp = f.read()

sys_name = None
port_id = None

for line in show_lldp.splitlines():
    if "System Name: " in line:
        s = line.split('System Name:')
        sys_name = s[1]
        print(sys_name)
    elif "Port id: " in line:
        port_id = line.split('Port id: ')[1]
        print(port_id)
    if sys_name and port_id:
        break

print()
        
"""
arp_table = [('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')]

for ip,mac in arp_table:
    # eliminate the period and convert to uppercase
    mac = mac.split(".")
    mac = "".join(mac)
    mac = mac.upper()

    new_mac = []
    while len(mac)>0:
        #take the first two entries only
        entry = mac[:2]
     #   print(entry)
     #eliminiate the first two numbers stored in entry now
        mac = mac[2:]
      #  print(mac)
      #store in new_mac list the individual entries, two at a time so that they can be joined later.
        new_mac.append(entry)
        
    new_mac = ":".join(new_mac)
    print(new_mac)

