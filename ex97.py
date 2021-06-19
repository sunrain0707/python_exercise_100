#97.从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。


fp = open('test_ex97.txt', "w+")
ch = ''
while '#' not in ch:
    fp.write(ch)
    ch = input('输入字符串:\n')

fp = open('test_ex97.txt', 'r')
print(fp.read())
fp.close()