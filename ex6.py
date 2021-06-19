#6.斐波那契数列：0、1、1、2、3、5、8、13、21、34、……

def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return Fibonacci(num-1) + Fibonacci(num-2)

x = 10
a=Fibonacci(x)
print(a)