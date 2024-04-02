# 綜合健康計算機 (BMI BMR TDEE)

def get_bmi(height, weight):
    height = height / 100
    bmi = weight / height ** 2
    bmi = round(bmi, 1) # 四捨五入到小數點後一位
    return bmi

def get_bmr(sex, height, weight, age):
    if sex=="男":
        bmr = 66 + 13.7 * weight + 5 * height - 6.8 * age
    else:
        bmr = 655 + 9.6 * weight + 1.8 * height - 4.7 * age
    bmr = round(bmr, 2) # 四捨五入到小數點後二位
    return bmr

def get_tdee(sex, height, weight, age, times):
    bmr = get_bmr(sex, height, weight, age)
    tdee = bmr * times
    tdee = round(tdee, 2) # 四捨五入到小數點後二位
    return tdee

print("歡迎使用綜合健康計算機~")
print("(1)計算BMI")
print("(2)計算BMR")
print("(3)計算TDEE")
number = input("請輸入你想要計算的項目 (輸入1 or 2 or 3)")
if number == "1":
    height = float(input("請輸入身高(cm):"))
    weight = float(input("請輸入體重(kg):"))
    bmi = get_bmi(height, weight)
    print(f"你的BMI是:{bmi}")
elif number == "2":
    sex = input("請輸入性別(男 or 女):")
    height = float(input("請輸入身高(cm):"))
    weight = float(input("請輸入體重(kg):"))
    age = int(input("請輸入年齡"))
    bmr = get_bmr(sex, height, weight, age)
    print(f"你的基礎代謝率BMR是:{bmr}")
elif number == "3":
    sex = input("請輸入性別(男 or 女):")
    height = float(input("請輸入身高(cm):"))
    weight = float(input("請輸入體重(kg):"))
    age = int(input("請輸入年齡"))
    print("(1)久坐、幾乎沒運動")
    print("(2)每周低強度運動1~3天")
    print("(3)每周中強度運動3~5天")
    print("(4)每周高強度運動6~7天")
    print("(5)勞力密集工作或是每天")
    exer = input("請選擇妳的運動量(輸入1~5)")
    times = 0
    if exer == "1":
        timees = 1.2
    elif exer == "2":
            timees = 1.375
    elif exer == "3":
            timees = 1.55
    elif exer == "4":
            timees = 1.725
    else:
        timees = 1.9
    tdee = get_tdee(sex, height, weight, age, times)
    print(f"你的總熱量消耗(TDEE)是:{tdee}")