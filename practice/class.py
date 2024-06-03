# 搞一个变量，变量里面存放一个人的名字，年龄，性别，特长
# 打印口头禅
# 打印自我介绍
# 类 对象  对象的模板

class People:
    def __init__(self, name, age, sex, techang, ktc, zwjs):
        self.name = name
        self.age = age
        self.sex = sex
        self.techang = techang
        self.ktc = ktc
        self.zwjs = zwjs

    def koutouchan(self):
        print(self.ktc)

    def ziwojieshao(self):
        print(self.zwjs)

caixukun = People('蔡徐坤', 23, '男',
                  ['唱', '跳','rap','篮球'],
                  '你干嘛哎哟','练习时长两年半')
wangziyi = People('王子异', 24, '男',
                  ['唱', '跳','rap','篮球'],
                  '梦想做说唱领袖','诞生于1996')
caixukun.koutouchan()
caixukun.ziwojieshao()
wangziyi.koutouchan()
wangziyi.ziwojieshao()
print(caixukun.techang)


