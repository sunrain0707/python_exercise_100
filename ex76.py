#76.编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

def even(n):
    sum1 = 0
    for i in range(2,n+1,2):
        sum1+=(1/i)
    return sum1

def odd(n):
    sum2 = 0
    for i in range(1,n+1,2):
        sum2+=(1/i)
    return sum2

x = int(input('number:'))
if x%2==0:
    y = even(x)
else:
    y = odd(x)

print(y)

print()