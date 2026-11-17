def transmission_type(ip):
   from ipaddress import ip_address
   ip_obj = ip_address(ip)
   if ip_obj.is_multicast:
       return "Multicast"
   elif ip_obj.is_unspecified or ip == "255.255.255.255" or ip_obj.packed[-1] == 255:
       return "Broadcast"
   else:
       return "Unicast"
# Test cases
print(transmission_type("192.168.1.10")) # Unicast
print(transmission_type("192.168.1.255")) # Broadcast
print(transmission_type("224.0.0.5")) # Multicast