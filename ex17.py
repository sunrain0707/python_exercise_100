#17.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。 条件为输入的字符不为 '\n'。

x = input('请输入字符：')
letters = 0
space = 0
digit = 0
others = 0
for i in x:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
    else:
        others+=1
print('letters=%d'%letters)
print('space=%d'%space)
print('digit=%d'%digit)
print('others=%d'%others)
