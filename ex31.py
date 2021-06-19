#31.请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

a = input('please input first letter of one day:')
if a=='S':
    b = input('please input second letter：')
    if b=='a':
        print('Saturday')
    elif b=='u':
        print('Sunday')
    else:
        print('false!!!')
elif a=='T':
    b = input('please input second letter：')
    if b=='u':
        print('Tuesday')
    elif b=='h':
        print('Thursday')
    else:
        print('false!!!')
elif a=='M':
    print('Monday')
elif a=='F':
    print('Friday')
elif a=='W':
    print('Wednesday')
else:
    print('false!!!')