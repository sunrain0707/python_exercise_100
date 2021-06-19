#49.使用lambda来创建匿名函数。

max = lambda x, y: (x > y) * x + (x < y) * y
min = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print('The largar one is %d' % max(a, b))
    print('The lower one is %d' % min(a, b))