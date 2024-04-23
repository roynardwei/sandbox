# practice1.把 52 74 8569 235 放在另一個列表里
# practice2.把 52 8569 48 放在另一個列表里
# practice3.把 data中的數據從小排到大
# practice4.判斷48在不再data中

data = [10, 42, 52, 74, 8569, 235, 48, 24646, 7757]

# 使用append放在列表
result = []
index = 2
while index <= 5:
    result.append(data[index])
    index += 1
print(result)

#使用切片放在列表(從左開始右邊不包含)data[開頭:結束:空幾格]
result = data[2:7:2]
print(result)

#排序練習 sort從小到大
data = [10, 42, 52, 74, 8569, 235, 48, 24646, 7757]
data.sort()
print(data)
data.sort(reverse=True) # 從大到小排序
print(data)

#判斷數值在不再列表 in
data = [10, 42, 52, 74, 8569, 235, 48, 24646, 7757]
result = 48 in data
print(result)
