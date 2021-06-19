#98.从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存

s = input('input a string:')
s = s.upper()

fp = open('test_ex98.txt', 'w')
fp.write(s)
fp = open('test_ex98.txt', 'r')
print(fp.read())
fp.close()