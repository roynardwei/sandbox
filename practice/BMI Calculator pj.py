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
bmi = round(bmi, 1)
print(f"你的BMI是:{bmi}")
if bmi < 18.5:
    print(f"你的BMI是:{bmi} (重過輕輕)")
# elif bmi >= 18.5 and bmi < 24:
elif bmi < 24:
    print(f"你的BMI是:{bmi} (正常體位)")
elif bmi < 27:
    print(f"你的BMI是:{bmi} (體重過重)")
elif bmi < 30:
    print(f"你的BMI是:{bmi} (輕度肥胖)")
elif bmi < 35:
    print(f"你的BMI是:{bmi} (中度肥胖)")
else:
    print(f"你的BMI是:{bmi} (重度肥胖)")