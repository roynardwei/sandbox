# # 函式(函數)function
# # 一定要做縮排 4空白 or 1 tab.
# # 參數可以使用指定 name="小綠" height=160, age=30,
# def print_info(name, age, height):
#     print(f"{name}今年{age}歲")
#     print(f"{name}身高{height}公分")
#
# print_info("小黑", 26, 176)
# print_info(name="小綠", age=30, height=181)
#
# # 測驗一
#
# def find_max(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         print(num1)
#     elif num2 > num1 and num2 > num3:
#         print(num2)
#     else:
#         print(num3)
#
#
# max = find_max(1, 2, 3)
#

# 函式迴傳 return

# def find_max(num1, num2, num3):
#     if type(num1) != int or type(num2) != int or type(num3) != int:
#         return "請輸入整數"
#     print("你好")
#     if num1 >=num2 and num1 >= num3:
#         return num1
#     elif num2 >=num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# max = find_max("你好", 20, 30)
# print(max)

# 測驗2

def find_max(num1, num2, num3):

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def find_min(num1, num2, num3):

    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3
def max_min (num1, num2, num3):
    if type(num1) != int or type(num2) != int or type(num3) != int:
        return "請輸入整數"
    else:
        return find_max(num1, num2, num3)- find_min(num1, num2, num3)
num = max_min(2, 5, 10)
print(num)
