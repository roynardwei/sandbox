# 作用域 範圍 前綴
# 全局作用域 不管在這個代碼文件的哪個地方都有機會訪問道
# 局部作用域 在代碼區塊裡面的變數
# 訪問一個變數 局部作用域> 全局作用域

a = 11 #全域.a
b = 21 #全域.b

def testfunc():
    global a #全域.a
    a = 10  #將全域.a改成10
    b = 20  #局域.b
    return a, b #全域.a 局域.b
c, d = testfunc()
print(a, b, c, d)