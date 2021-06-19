#1.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

list = [1,2,3,4]
b=[]

for i in list:
    for j in list:
        for k in list:
            if (i != j) and (j != k) and (i != k):
                x = i + 10*j + 100*k
                b.append(x)
print(b)
print(len(b))