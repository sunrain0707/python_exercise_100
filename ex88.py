#88.读取7个数（1—20）的整数值，每读取一个值，程序打印出该值个数的＊。

import random

for i in range(1,8):
    a = random.randint(0,20)
    print(i,':',a,'\n')
    print(a*'*')