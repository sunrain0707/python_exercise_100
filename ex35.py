#35.文本颜色设置。

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print (bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)

print('\033[30m黑色字体\033[0m')
print('\033[31m红色字体\033[0m')
print('\033[32m绿色字体\033[0m')
print('\033[33m黄色字体\033[0m')
print('\033[34m蓝色字体\033[0m')
print('\033[35m紫色字体\033[0m')
print('\033[36m青色字体\033[0m')
print('\033[37m白色字体\033[0m')
print('------------分割线----------------')
print('\033[40m黑色背景\033[0m')
print('\033[41m红色背景\033[0m')
print('\033[42m绿色背景\033[0m')
print('\033[43m黄色背景\033[0m')
print('\033[44m蓝色背景\033[0m')
print('\033[45m紫色背景\033[0m')
print('\033[46m青色背景\033[0m')
print('\033[47m白色背景\033[0m')

print('\033[0m默认亮度\033[0m')
print('\033[1m高亮显示\033[0m')
print('\033[4m下划线\033[0m')
print('\033[5m闪烁\033[0m')
print('\033[7m反取\033[0m')
print('\033[8m不显示\033[0m')