# 實現一個'今天吃什麼'的小程式
# '今天吃什麼'程式的功能很簡單，啟動程式後從妳喜歡的各種美食中
# 隨機挑選一個做為結果印出來

# 模塊 包 庫
# import random 整個函式庫引入


from random import choice, shuffle #指導入一些函式從random函式庫中

result = choice(['辣椒炒肉', '水煮魚', '豬肚雞', '拉麵', '咖哩飯', '炒麵'])
print(result)


dish1 = ['辣椒炒肉', '水煮魚', '豬肚雞', '拉麵', '咖哩飯', '炒麵']
shuffle(dish1) # 打亂順序
print(dish1)

import math
print(math.fabs(-10.223)) # 絕對值

import os.path
print(os.path.abspath('./'))
