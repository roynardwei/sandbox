# 函式(函數)function
# 一定要做縮排 4空白 or 1 tab.
# 參數可以使用指定 name="小綠" height=160, age=30,
def print_info(name, age, height):
    print(f"{name}今年{age}歲")
    print(f"{name}身高{height}公分")

print_info("小黑", 26, 176)
print_info(name="小綠", age=30, height=181)

# 測驗一

def find_max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)

find_max(1, 2, 3)
