#39.有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

a=[1,2,3,5,6,7]
k=len(a)
x=int(input('input a num:'))
a.append(x)
for i in range(1,len(a)):
    if x<a[len(a)-i]:
        a[len(a)-i+1]=a[len(a)-i]
        k=len(a)-i
a[k]=x
print(a)

