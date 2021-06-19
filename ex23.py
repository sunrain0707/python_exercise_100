#23.打印出如下图案（菱形）:

for i in range(1,5):
    print(' '*(4-i+1),end='')
    for j in range(i*2-1):
        print('*',end='')
    print()
for i in range(3, 0,-1):
    print(' ' * (4 - i + 1), end='')
    for j in range(i * 2 - 1):
         print('*', end='')
    print()
