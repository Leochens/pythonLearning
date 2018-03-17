#coding:utf-8

# 接下来说说python中的魔术方法

class Magic:

    # 对象描述方法
    def __str__(self):
        msg ='当你直接打印一个对象的时候我就会被调用'
        return msg

    def __idiv__(self, other):
        pass

    # 初始化方法
    def __init__(self):
        print('你创建对象的时候我就会被调用')
        pass

    def __del__(self):
        print('销毁对象的时候我就会被调用')
        pass

    # 相当于 ==
    def __eq__(self, other):
        return id(self) == id(other)

    # <
    def __lt__(self, other):
        pass
    # >
    def __gt__(self, other):
        pass
    # <=
    def __le__(self, other):
        pass
    # >=
    def __ge__(self, other):
        pass
    # +
    def __add__(self, other):
        pass
    # -
    def __sub__(self, other):
        pass
    # *
    def __mul__(self, other):
        pass
    # 取余 %
    def __divmod__(self, other):
        pass
    # / 真实的除法 带小数那种
    def __truediv__(self, other):
        pass

    # // 取整除法
    def __floordiv__(self, other):
        pass
    # 乘方
    def __pow__(self, power, modulo=None):
        pass
m = Magic()
x = m
print(m)

print(x==m)