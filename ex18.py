#18.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
x = int(input('请输入数字：'))
n = int(input('请输入个数：'))
sum = x
for i in range(1,n):
    t = x*10+x
    sum += t
print(sum)
