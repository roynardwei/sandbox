# 定義函數
# def 函數名(參數1, 參數2, 參數3, ..., n,):
#     代碼

# 使用函數
# 函數名(參數1, 參數2, 參數3, ..., n,)

def yayatest():
    print("耶耶")
yayatest()

def add(Num1:int, Num2:int=5)->int: # 函數的默認值 如果使用函數沒填參數就會直接使用默認值
    print(Num1+Num2)
add(1)


def add1(Num1:int, Num2:int=3)->int: # 使用return 可以把結果存到使用函數的地方 ，參數後面可以設定註解冒號
    return (Num1+Num2, Num1, Num2)

result = add1(6)
print(result)

# 練習 定義一個函數，該函數能夠判斷一個數是不是水仙花數
# 如果是水仙花數就返回true,否則就false
# 153 = 1*1*1 + 5*5*5 + 3*3*3
# 方式一
def is_iris(number:int)->bool:
    if number > 999 or number <100:
        return False
    number = str(number)
    gewei = int(number[2])
    shiwei = int(number[1])
    baiwei = int(number[0])
    if gewei**3 + shiwei**3 + baiwei**3 == int(number):
        return True
    return False
print(is_iris(153))

# 方式二
def is_iris2(number:int)->bool:
    if number > 999 or number <100:
        return False
    gewei = number %10 # 取餘數會剩下個位數
    shiwei = number //10 %10 # 整除後取餘數會剩下十位數
    baiwei = number //10 //10 %10 # 整除兩次後取餘數會剩下個位數
    if gewei**3 + shiwei**3 + baiwei**3 == number:
        return True
    return False
print(is_iris2(153))