#coding:utf-8

# 类与对象
# 简单点来说 类就是模板 对象就是实物
# 用模板来创造实物 就是初始化对象的过程

# 定义一个类

class Car:

    # 构造函数
    def __init__(self):
        # 属性 颜色
        self.color = 'red'

    # 方法
    def Run(self):
        print('Car Run ...')
    def openDoll(self):
        print('Car Open The Doll')

# 初始化一个类
car = Car()
print(car.color)

# 为这个对象添加一个独有属性 这一点和C C++ Java等不同
# 我把这叫做 按需添加 python是有这样的特性的
car.wheel=4

car.Run()
car.openDoll()
print(car.wheel)


