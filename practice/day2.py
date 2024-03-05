# 資料型態

# 字串 string
name = "你好"
print(name)
print("100"+"30")
#字串特別用法 加中括號
name = "你好小白"
print(name[3])

# 整數 int
num = 100
print(num)
print(100+30)
print(1_000_000)
# 浮點數 float
num1 = 160.57777
print(160.57777)
print(160.5+2.3)
print(num1)
# 布林值 boolean
is_male = True
False
print(is_male)
print(False)

#轉換資料型態
num1 = input("請輸入數字1:")
num2 = input("請輸入數字2:")
print(num1+num2)
print(type(num1)) #type函式可以檢查型態
print(type(num2))
#轉換成整數用int()函式
num1 =int(input("請輸入數字1:"))
num2 =int(input("請輸入數字2:"))
print(type(num1))
print(type(num2))
print(num1+num2)
#轉換成浮點數用float()函式
num1 =float(input("請輸入數字1:"))
num2 =float(input("請輸入數字2:"))
print(type(num1))
print(type(num2))
print(num1+num2)
#字串與數字相加str()函式
num1 = str(10)
print(type(num1))
print(num1+"你好")