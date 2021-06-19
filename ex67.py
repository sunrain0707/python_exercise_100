#67.输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

x = [312,432,435,534,5,25]
'''
for i in range(1,n+1):
    a = int(input('x:'))
    x.append(a)
'''
n = len(x)
max = x[0]
min = x[0]
mini = 0
maxi = 0
for j in range(len(x)):
    if x[j]>max:
        max=x[j]
        maxi=j
        print('max',x[j])
    if x[j]<min:
        min=x[j]
        mini=j
        print('min',x[j])
x[maxi],x[0] = x[0],x[maxi]
x[mini],x[n-1] = x[n-1],x[mini]
print(x)