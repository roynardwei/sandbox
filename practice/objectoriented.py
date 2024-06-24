# 物件導向三大特性 封裝 繼承 多態
# 封裝: 將物件屬性私有化, 不允許外部修改。 把共性(屬性, 函數)放一起成class
# 繼承: 子類繼承父類的屬性, 函數
# 多態: 同一個名字的函數, 擁有不同的效果

# Class的屬性 VS Object的屬性
# Class的屬性屬於Class, 並且所有該Class的object都共享這個屬性
# Object的屬性屬於Object self.XXXX


class Animal:
    Banimal = True;
    def __init__(self, name):
        self.__name = name #加上兩個下底線防止繼承
        print(self.__name, id(self.__name))
    def __eat(self): #函數也可以加上兩個下底線防繼承
        print("Animal的吃")
    def sound(self):
        pass

print (Animal.Banimal)
a1 = Animal('財')
a2 = Animal('白')
print(a1.Banimal)
a2.Banimal = False
print(a2.Banimal)

#
# class Dog(Animal):
#     def __init__(self):
#         super().__init__("小黃")
#     def sound(self):
#         print("汪汪")
#
# class Cat(Animal):
#     def __init__(self):
#         super().__init__("小黃")
#     def sound(self):
#         print("喵喵")
# def makesound(animal):
#     animal.sound()
#
# dog = Dog()
# cat = Cat()
# # dog.eat()
# # print(dog.name)
# makesound(dog) #多態
# makesound(cat)