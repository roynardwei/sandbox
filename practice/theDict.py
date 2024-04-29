# 字典 Key, Value,
# 姓名    數學  英文  社會
# Adby    85   50     88
# Ashely  95   85     90
# Cindy   80   75     85
# Dacy    95   90     95
# Ellen   85   80     90

# score_info = {"Abby":85, "Ashely":95}
# print(score_info["Ashely"]) #取得數據
# score_info["Abby"]=100 #修改數據
# print(score_info["Abby"])
# score_info["Cindy"]=80 #加進去一個KEY, VALUE
# print(score_info["Cindy"])
# score_info.pop("Abby")
# print(score_info)

#多個 Key, Value,
score_info = {"Abby":{"數學":80, "英文":100, "社會":80},   "Ashely":{"數學":60, "英文":67, "社會":80}}
print(score_info["Ashely"]["英文"])
