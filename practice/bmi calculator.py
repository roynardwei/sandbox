# BMI 計算機
# create by Roy wei 3/11

#公式BMI = w / h*2
height = float(input("輸入你的身高(公分)\n"))
# 輸入的是字串需要以Float轉成浮點
weight = float(input("輸入你的體重(公斤)\n"))
# 輸入的是字串需要以Float轉成浮點
height = height / 100
#轉換成公尺 height / = 100,另種寫法

bmi = weight / height**2
print(f"你的BMI是:{bmi}")
