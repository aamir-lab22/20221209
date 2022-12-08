#!/usr/bin/env python3


import math as m

data = [41844, 41500, 39995, 36995, 40990, 37995, 41995, 38900, 42995, 36995, 43995, 35950]
mean = sum(data)/len(data)
print(mean)
diff = [i - mean for i in data]
print(diff)
diff2 = [i**2 for i in diff]
print(diff2)
stdev = m.sqrt(sum(diff2)/(len(data) - 1))
print(stdev)
