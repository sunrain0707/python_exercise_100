#69.有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
data = [i+1 for i in range(20)]
print(data)
i = 1
while len(data) > 1:
    if i % 3 == 0:
        data.pop(0)
    else:
        data.insert(len(data),data.pop(0))
    i += 1
print(data)