#10.暂停一秒输出，并格式化当前时间。

import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
time.sleep(1)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

'''
%Y—年份
%m–月份
%d–天数
%H–小时
%M–分钟
%S–秒数
'''