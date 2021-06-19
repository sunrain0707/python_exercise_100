#16.输出指定格式的日期。使用 datetime 模块。

import time

print(time.time())
print(time.localtime())
print(time.asctime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

import datetime

print(datetime.date.today())
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.date(1998, 7, 7))


# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print('1:',datetime.date.today().strftime('%d/%m/%Y'))
# 创建日期对象
BirthDate = datetime.date(1998, 7, 7)
print('2:',BirthDate.strftime('%d/%m/%Y'))
# 日期算术运算
BirthNextDay = BirthDate + datetime.timedelta(days=1)
print('3:',BirthNextDay.strftime('%d/%m/%Y'))
# 日期替换
FirstBirthday = BirthDate.replace(year=BirthDate.year + 1)
print('4:',FirstBirthday.strftime('%d/%m/%Y'))

#if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。

