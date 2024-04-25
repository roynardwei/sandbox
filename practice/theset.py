# 集合 無秩序 沒有重複值的列表
data = {245, 7, 27, 8, -1,}
print(type(data))
print(data)
print(len(data))
data.add(9)
print(data)
data.remove(9)
print(data)
print(7 in data)
# 交集 聯集 減法
data2 = {245, 7, 27, 136, 8, -1, 10, 2, 25, 1}
print(data.intersection(data2))
print(data.union(data2))
print(data.difference(data2))