#20.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？
# 第10次反弹多高？

def hight(n):
    if n == 0:
        return 100
    return hight(n-1)/2

sum = 100
for i in range(0,11):
    sum +=hight(i)
print(hight(10))
print(sum)

