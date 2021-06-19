#85.输入一个奇数，然后判断最少几个 9 除于该数的结果为整数

x = int(input('input an odd:'))
flag = True
i = 1
y = 9

while flag:
    if y%x==0:
        break
    else:
        i+=1
        y = (y*10)+9

print(i)
print(y,'/',x,'=',y//x)