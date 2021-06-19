#12.判断101-200之间有多少个素数，并输出所有素数。
import math

x = True
for i in range(101,200):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j == 0:
            x = False
    if x == True:
         print(i)
    x = True