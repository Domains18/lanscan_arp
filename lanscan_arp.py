import scapy.all as scapy
import re
print("\n**************************************************************************")
print("\n* To Whom much Has been Given, much is expected                           *")
print("\n* https://github.com/Domains18                                            *")
print("\n***************************************************************************")

ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
while True:
    ip_add_range_entered = input("Enter the IP address range to scan: ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"IP address range entered is valid: {ip_add_range_entered}")
        break
    
arp_result = scapy.arping(ip_add_range_entered)