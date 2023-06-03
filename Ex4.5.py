command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
list_vlan1 = command1.split()
list_vlan2 = command2.split()
vlan1 = set(list_vlan1[-1].split(','))
vlan2 = set(list_vlan2[-1].split(','))
inbox = (set(vlan1.intersection(vlan2)))
result = (sorted(inbox))
print(result)
