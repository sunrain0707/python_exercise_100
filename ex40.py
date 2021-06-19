#40.将一个数组逆序输出

a = [43,47,23,76,314,76,23,5]
n = len(a)
print(a)
for i in range(0,len(a)//2):
    a[i],a[n-i-1]=a[n-i-1],a[i]
print(a)