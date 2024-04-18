# 找出列表中的最小值
data = [10, 5, 3, 4, 5, -6, 7, 8, 9]
min_value = data[0]
index = 1
print(type(index))
while index < len(data):
    if data[index] < min_value:
        min_value = data[index]
    index += 1
print(min_value)

# 方法二 使用min函式
data2 = [100, 95, 60, 7, -1090, 125]

minvalue=min(data2)

print(minvalue)

