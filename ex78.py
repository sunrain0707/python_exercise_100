#78.找到年龄最大的人，并输出。请找出程序中有什么问题。

person = {"hsy": 22, "hcc": 23}
m = 'hsy'
for key in person.keys():
    if person[m] < person[key]:
        m = key

print('%s是那个更老的一个，今年%d' % (m, person[m]))
