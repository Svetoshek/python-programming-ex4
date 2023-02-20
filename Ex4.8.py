ip = "192.168.3.1"
new = ip.split(".")
print("""{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}"""
      .format(int(new[0]),int(new[1]),int(new[2]),int(new[3]),
              int(new[0]),int(new[1]),int(new[2]),int(new[3])))

