'''企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？'''

'''
I = int(input('请输入当月利润（万元）：'))
money = 0
if I <= 10:
    money = I * 0.1
elif (I > 10) and (I < 20):
    money = 10*0.1 + (I-10)*0.075
elif (I > 20) and (I < 40):
    money = 10*0.1 + 10*0.075 + (I-20)*0.05
elif (I > 40) and (I < 60):
    money = 10*0.1 + 10*0.075 + 20*0.05 + (I-40)*0.03
elif (I > 60) and (I < 100):
    money = 10*0.1 + 10*0.075 + 20*0.05 + 20*0.03 + (I-60)*0.015
elif I >= 100:
    money = 10*0.1 + 10*0.075 + 20*0.05 + 20*0.03 + 40*0.015 + (I-100)*0.01
print('奖金数：' + str((money)))   
'''

i = int(input('请输入当月利润（万元）：'))
arr = [100,60,40,20,10,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for n in range(0,6):
    if i>arr[n]:
        r+=(i-arr[n])*rat[n]
        i=arr[n]
print('奖金数：' + str(r))