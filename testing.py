networks_highest_pref = \
    [{'network': '192.168.1.0', 'netmask': '255.255.255.0', 'localpref': 100, 'ASPath': [1], 'origin': 'EGP',
      'selfOrigin': True, 'peer': '192.168.0.2'},
     {'network': '172.169.0.0', 'netmask': '255.255.0.0', 'localpref': 100, 'ASPath': [2], 'origin': 'EGP',
      'selfOrigin': True, 'peer': '172.168.0.2'},
     {'network': '11.0.0.0', 'netmask': '255.0.0.0', 'localpref': 100, 'ASPath': [3], 'origin': 'EGP',
      'selfOrigin': False, 'peer': '10.0.0.2'}]

for network in networks_highest_pref:
    if not network['selfOrigin']:
        networks_highest_pref.remove(network)

print(networks_highest_pref)