# 1.写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等),
# 将每个实参的每个元素依次添加到函数的动态参数args里面.
# 例如 传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
# def func(*args):
#     return args
#
#
# res = func(*[1,2,3], *(22,33))
# print(res)


# def func(*args):
#     li = []
#     for i in args:
#         for j in i:
#             li.append(j)
#     return tuple(li)
#
# res = func([1,2,3], (22,33))
# print(res)




# 2.写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面.
# 例如 传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}
# def func(**kwargs):
#     return kwargs
#
#
# print(func(**{'name': 'alex'}, **{'age': 1000}, **{'hobby': '打球'}))


# 3.写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)
# def min_max(*args):
#     print(args)
#     max_var = max(args)
#     min_var = min(args)
#     print(max_var, min_var)
#     return {'max': max_var, 'min': min_var}
#
#
# print(min_max(2, 5, 7, 8, 4), 111111)
#
#
# def min_max(*args):
#     li = list(args)
#     li.sort()
#     max_var = li[-1]
#     min_var = li[0]
#     return {'max': max_var, 'min': min_var}
#
#
# print(min_max(2, 5, 7, 8, 4), 111111)


# 4.写函数，传入一个参数n，返回n的阶乘(普通方法)
# 例如:cal(7)  计算7*6*5*4*3*2*1
# def cal(n):
#     count = 1
#     for i in range(n, 0, -1):
#         print(i)
#         count *= i
#     return count
#
#
# while 1:
#     n = input('>>>').strip()
#     res = cal(int(n))
#     print(res)

# count = 1
# def func(n):
#     if n:
#         func(n - 1)
#         global count
#         count *= n
#     print(count)
# func(7)

# def func(n):
#     if n == 1:
#         return 1
#     return n * func(n - 1)
# res = func(7)
# print(res)


# count = 3
# while count:
#     print(123)
#     count -= 1
# print(456)



# 5.写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组（升级题）
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]

# def func():
#     lis = ['黑桃', '红心', '梅花', '方块']
#     lis2 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
#     li = []
#     for i in lis2:
#         for j in lis:
#             li.append((j, i))
#     return li
#
#
# print(func())




# 6.下面代码成立么?如果不成立为什么报错?怎么解决?
# 1
# a = 2
# def wrapper():
#     print(a)
# wrapper()


# 2
# a = 2
# def wrapper():
#     a += 1
#     print(a)
# wrapper()

# a = 2
# def wrapper():
#     global a
#     a += 1
#     print(a)
# wrapper()


# 3

# def wrapper():
#      a = 1
#      def inner():
#          print(a)
#      inner()
# wrapper()

# 4
# def wrapper():
#      a = 1
#      def inner():
#          a += 1
#          print(a)
#      inner()
# wrapper()


# def wrapper():
#      a = 1
#      def inner():
#          nonlocal a
#          a += 1
#          print(a)
#      inner()
# wrapper()




