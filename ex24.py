#24.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
sum = 0
for i in range(1,21):
    sum+=(fib(i+2))/(fib(i+1))

print(sum)