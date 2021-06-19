#95.字符串日期转换为易读的日期格式

import time

start = time.time()
for i in range(3000):
    print(i)
end = time.time()
print(end - start)

print(time.ctime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.asctime(time.gmtime(time.time())))

import datetime

print(datetime.date.today())
print(datetime.date.today().strftime('%d/%m/%Y'))