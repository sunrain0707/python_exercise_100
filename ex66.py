#66.输入3个数a,b,c，按大小顺序输出

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

x = [a,b,c]
x.sort()
x.reverse()
print(x)