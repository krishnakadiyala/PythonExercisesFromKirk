"""f = open("new.txt")

output = f.read()

print(type(output))

print(output)

f.close()

Another way to read a file - using a context manager form

with open("new.txt") as f:
    output = f.readlines()

print(type(output))

Python automatically closes the file, we don't have to explicitly close the file.

Exercise2:

my_list = ['192.124.1.2', '145.62.71.98']

print(len(my_list))

my_list.append('12.143.121.1')

my_list.extend(['121.19.90.1', '192.123.45.6'])

print(my_list[0])

my_list.pop(0)

my_list.pop(len(my_list)-1)

print(my_list)

my_list[0] = '2.2.2.2'

print(my_list)

Exercise 3:

with open("show_arp.txt") as f:
    output = f.readlines()

output = output[1:]

#from pprint import pprint
#pprint(output)

output.sort()

my_entries = output[:3]

print(my_entries)

my_entries = "\n".join(my_entries)

print(my_entries)

with open("new.txt", "wt") as f:
    f.write(my_entries)

Exercise 4:s

with open("show_ip_int_brief.txt") as f:
    output = f.readlines()

entry = output[5].split()

ip = entry[0]
int = entry[1]

my_tuple = (int, ip)

print(my_tuple)

Exercise 5:
"""

with open("show_ip_bgp_summ.txt") as f:
    output = f.read()

output = output.splitlines()

first = output[0]
last = output[-1]

asn = first.split()[-1]
peer_ip = last.split()[0]
print("Local AS number: {}".format(asn))
print("BGP peer IP address: {}".format(peer_ip))
