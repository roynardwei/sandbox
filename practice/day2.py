# 資料型態
# create by Roy wei 24/3/5


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

#測試一
num = input("請輸入一個兩位數數字:")
digit1 = float(num[0])
digit2 = float(num[1]) #可使用float 轉成小數點#

print(type(digit1))
print(type(digit2))
print(digit1+digit2)

# 一些字串的用法放引號,換行,
print('他今年"25"歲')
print("他今年\"25\"歲")

print("大家好我是小白\n今天天氣真好")
age = 25
height = 175.5
is_male = True
print("小白的年紀是"+ str(age) +"歲，身高"+ str(height) +"CM，是否為男性:"+str(is_male))
f-string # 在字串最前面加f 字串中的變數可以加上大括號
print(f"小白的年紀是{age}歲，身高{height}CM，是否為男性:{is_male}")