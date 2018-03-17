#coding:utf-8


# 父类
class Friut:

    name = 'fruit'

    def sayname(self):
        print(self.name)

# 子类 括号里写父类名字
class Apple(Friut):
    name = 'apple'


apple = Apple()

# 调用父类方法
apple.sayname()