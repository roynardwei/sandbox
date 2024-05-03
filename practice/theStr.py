# 再見字串
data1 = '喔妳 實在太美哦BABY'
data2 = "喔妳 實在太美哦BABY"
data3 ="""
喔妳
實在太美
哦BABY
"""
print(len(data1))
print(id(data1))
print(data1[:2])
result = data1.replace("喔","oh")
print(result)
print(id(result))

index = data1.find("BABY")
print(index)
print(data1.split(" "))

# 字串做加法和減法
data = '妳'+'幹'+'麻'
print(data)
data += data1
data = "喔"*5
print(data)

# 格式化字串
# 1.佔位式
# %d 整數
# %f 小數
# %s 字串
name = "張先生"
number = 888
data = '您好，尊貴的%s，您預約的%d號技師馬上就到，請稍後' % (name,number)
print(data)

# 2.format .直接使用花括號就可以取代格子
name1 = "Roy"
number1 = 793
data = '您好，尊貴的{}，您預約的{}號技師馬上就到，請稍後'.format(name1, number1)
print(data)

# 3.f-string .前面加上f 格子換成花括號
name3 = "Wei"
number3 = 987
data = f'您好，尊貴的{name3}，您預約的{number3}號技師馬上就到，請稍後'
print(data)