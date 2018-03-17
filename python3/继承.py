#coding:utf-8


# 父类
class Friut:

    name = 'fruit'

    def sayname(self):
        print(self.name)
    def hello(self):
        print('hello i am {}'.format(self.name))

# 子类 括号里写父类名字
class Apple(Friut):

    # 重写父类属性
    name = 'apple'

    # 重写父类方法
    def hello(self):
        super().hello()         #调用父类的方法
        print('there is child')

apple = Apple()

# 调用父类方法
apple.sayname()

# 调用重写后的父类方法

apple.hello()