#coding:utf-8

# 列表推导式怎么玩呢？
# 所谓列表推导 就是说根据线索和一定条件来进行一个推导 最后给我生成一个列表

# 看个例子
# 输出范围0~5的整形数
list = [li for li in range(0,5) ]   # range(5)也可以 range()自动从0开始
print(list)                         # [0, 1, 2, 3, 4]

# 说明：
# 把li作为推导元 让li在0~5的范围内推导 所以每进行一次循环 list就加入一个元素
# 而这个元素就是符合推导条件的

list_if = [ li for li in range(3,8) if li%2 == 0 ]
print(list_if)

# 说明：
# 这是一个条件推导 只有在for循环里满足li%2==0这个条件的li才能被增加到list_if这个列表中

list_2_for = [ [a,b] for a in range(3) for b in range(4)]
print(list_2_for)

# 说明：
# 这是一个双层循环推导式 返回的是元素为2元祖的列表 元素个数为 3 *4 = 12个
# 类似可以进行n层循环

# 如下
list_4_for = [ [a,b,c,d] for a in range(3)
               for b in range(4)
               for c in range(2)
               for d in range(3) ]
print(list_4_for)

# 例题
# 请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]

m = [ li for li in range(1,101) ]   # 待分组的
n = [ m[x:x+3] for x in range(0,100,3)]# 按照三个一组
print(n)