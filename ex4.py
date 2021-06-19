#4.输入某年某月某日，判断这一天是这一年的第几天？

year = int(input('年：'))
month = int(input('月：'))
day = int(input('日：'))
sum = 0

if ((year%4 == 0 and year/100 != 0) or (year/400 == 0)) and (month > 2):
    sum = -1
elif month>2:
    sum = -2
x = int((month-1)/2)
sum += (month-1)*31 + day - x

print( str(month) + '月' + str(day) + '日是' + str(year) +'年的第' + str(sum) + '天' )

