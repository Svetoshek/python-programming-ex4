mac = "AAAA:BBBB:CCCC"
address = mac.split(":")
num_1 = (int(address[0],16))
num_2 = (int(address[1],16))
num_3 = (int(address[2],16))
bin_1 = (bin(num_1).replace("0b",""))
bin_2 = (bin(num_2).replace("0b",""))
bin_3 = (bin(num_3).replace("0b",""))
print(bin_1+bin_2+bin_3)