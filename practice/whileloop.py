# 練習一:打印10次 妳太美
# 循環 做重複勞動
count = 0
while count < 10:
    print("妳太美")
    count +=1

# 練習二:計算1+2+3+4+....+99+100
sum = 0
number = 1
while number <= 100:
    sum += number
    number +=1
print(sum)

# 練習三:打印1~100之間的所有奇術


number = 1
while number <= 100:
    if number % 2 == 1:
        print(number)
    number += 1