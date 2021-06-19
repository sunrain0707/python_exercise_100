#90.列表使用实例

# list
# 新建列表
l = [10086, '中国移动', [1, 2, 4, 5]]
print(l)
print(l[-1])
# 弹出列表的最后一个元素
print(l.pop(-1))
print(l)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix)
print(matrix[1])
col2 = [row[1] for row in matrix]  # get a  column from a matrix
print(col2)
col2even = [row[1] for row in matrix if row[1] % 2 == 0]  # filter odd item
print(col2even)