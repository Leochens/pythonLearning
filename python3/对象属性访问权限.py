#coding:utf-8

class Demo:

    # 带两个下划线的属性或方法是私有的 否则就是共有的
    __private = 'private'
    public = 'public'

    def __pri(self):
        pass
    def pub(self):
        pass

print(Demo.public)

#print(Demo.__private) # 报错