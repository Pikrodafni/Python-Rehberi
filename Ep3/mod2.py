import Ep3
# help(Ep3)
l = [100,200,300,400,500,600]
key = 500
print(Ep3.binary_search(l,key))
"""
uzun yorum satırını da bulduk
"""

# RE

import re

s = "ABCDE1234A"
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
l = re.findall(r,s)
print(l)

s = "8123456789"
r = re.compile("[6-9][0-9]{9}")
l = re.findall(r,s)
print(l)