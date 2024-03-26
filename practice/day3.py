# if 語句
# 條件都要四個空白或是tab鍵

# 如果 今天下雨:
#     我就開車去上班
# 否則:
#     我就走路去上班
#
# is_rainy = False
# if is_rainy:
#     print("我就開車去上班")
# else:
#     print("我就走路去上班")

# 如果 今天考試分數大於60分:
# 今天準備吃好料
# 否則 :
#      你今天準備罰跪

# score = 60
#
# if score>=60:
#     print("今天準備吃好料")
# else:
#     print("你今天準備罰跪")

# 如果 你的名字叫做林鮭魚的話:
#     鮭魚免費吃到飽
# 否則:
#     請付錢
# 判斷左右兩邊的東西是相等的要用 ==


# name = "林鮭魚"
# print(name != "林鮭魚")
# if name == "林鮭魚":
#     print("鮭魚免費吃到飽")
# else:
#     print("請付錢")

# 邏輯運算(and、or、not)

# 如果 分數1考100分 且 分數2考100分:
#     我給你100元
#     我帶妳出去玩

# score1 = 100
# score2 = 100
# print(True and True)
# if score1 == 100 and score2 == 100:
#     print("我給你100元")
#     print("我帶妳出去玩")

# 如果 分數1考100分 或 分數2考100分:
#     我給你100元
#     我帶妳出去玩
# score1 = 90
# score2 = 80
# if score1 == 100 or score2 == 100:
#     print("我給你100元")
#     print("我帶妳出去玩")
# else:
#     print("都沒考100分")

# not 邏輯運算 兩種都沒有符合達成否定
# 如果 分數1沒有考大於80分:
#     你給我100元
#if not score1 >80:也可寫 score1 <= 80: 這樣寫比較好理解

score1 = 80
if not score1 > 80:
    print("你給我100元"
          "")