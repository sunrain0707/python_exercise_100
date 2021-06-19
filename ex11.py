#11.古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

def rab(num):
    if num == 1 or num == 2:
        return 1
    return rab(num-1)+rab(num-2)

print(rab(12))
