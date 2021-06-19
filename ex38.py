#38.求一个3*3矩阵主对角线元素之和。

a=[[1,2,3,],[4,5,6],[7,8,9]]
sum=0
for i in range(0,3):
    sum+=a[i][i]
print(sum)
