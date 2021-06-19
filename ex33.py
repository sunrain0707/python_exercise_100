#33.按逗号分隔列表。

l = [1,2,3]
for i in l[0:len(l)-1]:
    print(i,end=',')
print(i+1)
