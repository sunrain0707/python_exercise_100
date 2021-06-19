#100.列表转换为字典。

l = [1,2]
L = ['a','b']
b = dict([l,L])
print(b)


key = ['a','b','c']
value = [1,2,3]
b=dict(zip(key,value))
print(b)


key = ['a','b','c']
value = [1,2,3]
b = {}
for i in range(len(key)):
    b.setdefault(key[i],value[i])
print(b)