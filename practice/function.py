# 定義函數
# def 函數名(參數1, 參數2, 參數3, ..., n,):
#     代碼

# 使用函數
# 函數名(參數1, 參數2, 參數3, ..., n,)

def yayatest():
    print("耶耶")
yayatest()

def add(Num1, Num2=5): #函數的默認值 如果使用函數沒填參數就會直接使用默認值
    print(Num1+Num2)
add(1)


def add1(Num1, Num2=3): #使用return 可以把結果存到使用函數的地方
    return (Num1+Num2, Num1, Num2)

result = add1(6)
print(result)