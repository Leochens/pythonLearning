#coding:utf-8

# set是一集合类型
# 所谓集合 就是说这个集合中没有重复的元素存在
# 所以利用这个特性 我们可以把一个列表或一个元组去重

list = [1,1,1,1,2,3,3,56,56,5,989,56,66,6,6,7,5,9]

list2set =  set(list)

print(list2set)# {1, 2, 3, 66, 5, 6, 7, 9, 56, 989}
print(type(list2set))# <class 'set'>