ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
list_route = ospf_route.split()
int = list_route[1].replace("]","").replace("[","")
print("""Prefix              {}
AD/Metric           {}  
Next-Hop            {} 
Last update         {}
Outbound Interface  {}
""".format(list_route[0],(int),
           list_route[3].replace(",",""),
           list_route[4].replace(",",""),
           list_route[5]))
