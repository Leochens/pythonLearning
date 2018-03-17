#coding:utf-8

# 不可变类型 int float tuple str 
#####################################################


a = 15
print("a-id:",id(a),"\n a = ",a)
b = a
print("b-id:",id(b),"\n b = ",b)

#现在改变a的值
a = 16

#a=16 a的id改变了
print("a-id:",id(a),"\n a = ",a)

#b=15 b的id没有变
print("b-id:",id(b),"\n b = ",b)

'''
a-id: 496882960 
 a =  15
b-id: 496882960 
 b =  15
a-id: 496882976 
 a =  16
b-id: 496882960 
 b =  15
'''


# 总结 ：
# int long bool
# float string tuple类型的变量值不可变

# 也就是在进行b=a等号赋值操作时 以上变量会指向同一个id地址 但当改变某一个变量的值时
# 被改变的变量会再去开辟一块空间存改变后的值 随后指针指向这个新得空间
# 没有被更改的变量还是指向原来的地址
# a , b 都拥护一个石头 突然有一天b不拥护它了 那么b就只能离开原来那个石头 去找新的石头


# 可变类型 list dict
#####################################################

list1  = [1,2,3,4]
list2 = list1

# 此时 list1，list2地址一样 值也一样
print('list1-id: ',id(list1),list1)
print('list2-id: ',id(list2),list2)

# 现在使list1增加一个元素6
list1.append(6)

# 增加完后list1和list2的地址还一样并且不变但是值都变了
# 也就是说list1的操作是指向这个地址的值的改变 并不改变指针
print('list1-id: ',id(list1),list1)
print('list2-id: ',id(list2),list2)

# 总结 ：
# list dict 类型都是可变类型 改一个就都改了 牵一发而动全身
# list1 和 list2 都拥护石头A 有一天 list1 不拥护它了改去拥护石头B 那么同时list2看到了 也不拥护石头A了
# 那么这俩人要做的 是把石头A换掉 把原来石头A的地方换成新的石头B
'''
list1-id:  44984040 [1, 2, 3, 4]
list2-id:  44984040 [1, 2, 3, 4]
list1-id:  44984040 [1, 2, 3, 4, 6]
list2-id:  44984040 [1, 2, 3, 4, 6]

'''

