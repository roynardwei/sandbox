#元祖 不能被修改的列表 地址不會變 只有值可以改
data = (112, 6, [1,2,3,4,5], 34, 63, 2522)
index = 0
while index < len(data):
    print(id(data[index]))
    index += 1
hahaha = [1,2,3,4,5]
print(id(hahaha))
data[2][3] = 6
print(data)
index = 0
while index < len(data):
    print(id(data[index]))
    index += 1
