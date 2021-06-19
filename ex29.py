#29.给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

x = int(input('输入数字：'))
a = []
sum = 0

while x!=0:
    a.append(x%10)
    sum+=1
    x = int(x/10)
print(sum)
print(a[:])
