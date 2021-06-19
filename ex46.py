#46.求输入数字的平方，如果平方运算后小于 50 则退出。

f = True
while f:
    x = int(input('input a number:'))
    cul = x*x
    if cul<50:
        f = False
        print('exit')
