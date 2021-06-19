#26.利用递归方法求5!。
def cul(n):
    if n==1:
        return 1
    return cul(n-1)*n

print(cul(5))