#61.打印出杨辉三角形

def Yang(num):
    if num == 1:
        return {1:1}
    if num == 2:
        return {1:1,2:1}
    x = {}
    y = Yang(num-1)
    x[1] = 1
    for i in range(2,num):
       x[i] = y[i-1] + y[i]
    x[num] = 1
    return x

num = 10
for i in range(1,num+1):
    yang = Yang(i)
    for v in yang.values():
        print(v,end='  ')
    print()
