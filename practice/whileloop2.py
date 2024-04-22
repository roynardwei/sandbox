# 計算 1!-2!+3!-4!+.....+49!-50!
# 循環 4!=1*2*3*4
#   判斷當前數字是不是偶數
#       循環
#       -數字的階乘
#   否則
#       循環
#       +數字的階層
#
# sum = 0
# number = 1
# while number <= 50:
#     result = 1
#     i = 1
#     while i <= number:
#         result *= i
#         i += 1
#     if number % 2 == 0:
#         sum -= result
#     else:
#         sum += result
#     number += 1
# print(sum)

# 輸出100以內的所有質數(質數是只能被1和它本身整除的數如3.5.7.11)
# 循環2到100
#   判斷當前的數字是不是質數
#   印出
# break跳出當前循環
# continue跳出當前迴圈，跳到下一個迴圈


#
# number = 2
# while number <= 100:
#     i = 2
#     is_prime = True
#     while i < number:
#         if number % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         print(number)
#     number += 1

# 輸出100以內的所有質數(質數是只能被1和它本身整除的數)
# 循環2到100(遍歷)
#   判斷當前的數字是不是質數(循環)
#   印出
#break跳出當前循環
#continue跳出當前迴圈，跳到下一個迴圈
# number = 6
# i = 2
# is_prime = True
# while i < number:
#     if number % i == 0:
#         is_prime = False
#         break
#     i += 1
# print(is_prime)

number = 2
while number <= 100:
    i = 2
    is_prime = True
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(number)
    number += 1

#
# num = [];
# i = 2
# for i in range(2, 100):
#     j = 2
#     for j in range(2, i):
#         if (i % j == 0):
#             break
#     else:
#         num.append(i)
# print(num)