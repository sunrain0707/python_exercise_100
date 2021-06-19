#30.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

x = int(input('输入数字：'))
a = str(x)
index = True
for i in range(int(len(a)/2)):
    if a[i]!=a[-i-1]:
        index = False
if index == True:
    print('yes')
else:
    print('no')