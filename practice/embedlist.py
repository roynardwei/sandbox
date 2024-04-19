# 二維列表
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

data2 = [[1,2,13,4],[25,-6,7,8],[99,10,11,12]]
maxvalue = data2[0][0]
r = 0
c = 0
while r < len(data2):
    c = 0
    while c < len(data2[r]):
        if data2[r][c] > maxvalue:
            maxvalue = data2[r][c]
        c += 1
    r += 1
print(maxvalue)