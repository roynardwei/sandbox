data = [25, [233, 888], {1, 2, 3}, "只因", {"name": "張三", 'age': 23}]
for d in data[2]:
    print(d)

#拿到key, value
for d in data[4].items():
    print(d)
#拿到值
for d in data[4].values():
    print(d)
#取範圍
for d in range(1,20,2):
    print(d)
#取得標籤 使用列舉enumerate
for d1 in enumerate(data):
    print(d1)

for index, d1 in enumerate(data):
    print(index)
    print(d1)

#建立一個列表,列表數據是1到30的整數
data2 = []
for number in range(1, 31):
    data2.append(number) #.append增加項目
print(data2)
#建立一個列表,列表數據是1到30的整數 以生成方式
data2 = [number for number in range(1, 31)]
print(data2)