#coding:utf-8

# 字符串格式化输出
age = 22
name = 'Leochens'

# ugly
print('my name is '+name+' , and I am '+ str(age)+ ' years old. ')

# good
print('my name is {0} , and I am {1} years old. '.format(name,age))

# better & best
print('my name is {} , and I am {} years old. '.format(name,age))

