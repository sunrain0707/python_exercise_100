#68.有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数

a = [1, 2, 3, 4, 5]
m = 3                  # 设置向后移动 3 位
for _ in range(m):
    a.insert(0, a.pop())
print(a)