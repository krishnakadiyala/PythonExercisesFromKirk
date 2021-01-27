"""
Krishna's solutions to exercises

Exercise1:
ip_addr1 = "118.12.6.34"
ip_addr2 = "192.123.26.1"
ip_addr3 = "128.12.98.45"

print(ip_addr1, ip_addr2, ip_addr3)
"""

""" Exercise 2:
ip_addr = input("Enter an IP address:")

octets = ip_addr.split(".")

print("{:^20}{:^20}{:^20}{:^20}".format('Octet1', 'Octet2', 'Octet3', 'Octet4'))
print("-" * 80)
print("{:^20}{:^20}{:^20}{:^20}".format(octets[0], octets[1], octets[2], octets[3]))
print("{:^20}{:^20}{:^20}{:^20}".format(hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))
print("{:^20}{:^20}{:^20}{:^20}".format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))      
"""

"""
Exercise 3:
ipv6_addr1 = "2001:db8:1234::1"
IPV6_ADDR2 = "2001:db8:1234::2"
ipV6_addR3 = "2001:db8:1234::3"

print("")
print("Is variable1 equal to variable2 : {}".format(ipv6_addr1==IPV6_ADDR2))
print("Is variable1 not equal to variable3 : {}".format(ipv6_addr1!=ipV6_addR3))
print("")
"""

show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "

show_version = show_version.strip()

fields = show_version.split()
model = fields[1]
serial_number = fields[2]

print()
print(fields)
print()

vendor_cisco = "cisco" in model.lower()
print("Checking if model contains Cisco : {}". format(vendor_cisco))

model_881 = "881" in model
print("Checking if model contains 881 : {}". format(model_881))

print("Serial number: {}".format(serial_number))
print("Model: {}". format(model))
print()


