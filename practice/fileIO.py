#文件讀寫 三板釜
#1.打開文件
#read. write. rb. wb. a.
# f = open('./class.py','r', encoding="utf8")

f = open('test.txt', 'w', encoding="utf8") #寫

# f = open('test.txt', 'a', encoding="utf8") #追加

# with open('test.txt', 'w', encoding="utf8") as f:   #使用with關鍵字可以避免忘記關閉文件
#     f.write("Roy practice\n")  # 寫入文件
#     f.write("Roy OK")
#     f.writelines(["請大家多多支持", "免費不易"])

with open("C:/users/ywei29/downloads/771.png", "rb") as f:  #複寫一個圖片文件
    data = f.read()
    with open("C:/users/ywei29/downloads/771_backup.png", 'wb') as ff:
        ff.write(data)
#2.讀取文件
# print(f.read()) #讀整個文件

# print(f.readline()) #一行行的讀文件
# print(f.readline())

# while True:   #用循環打印直到空字串
#     data = f.readline()
#     if len(data) == 0:
#         break
#     print(data)
#
# data = f.readlines()
# print(data)
# f.write("Roy practice\n") #寫入文件
# f.write("Roy OK")
# f.writelines(["請大家多多支持","免費不易"])
# f.close()
#
# while True:
#     pass

#3.關閉文件
# f.close()