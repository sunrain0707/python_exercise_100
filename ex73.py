#73.反向输出一个链表

if __name__ == "__main__":
    p = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        p.append(num)
        p.reverse()
    print(p)