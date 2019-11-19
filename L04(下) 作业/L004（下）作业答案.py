# 第一题
# name = ['oldboy', 'alex', 'wusir']

# def func(n):
#     return n + '_leader'
#
# it = map(func, name)
# print(list(it))

# it = map(lambda n: n + '_leader', name)
# print(list(it))

# 第二题
# listvar = [{'name':'alex'},{'name':'wusir'}]

# def func(n):
#     return n['name'] + '_leader'
#     # for k, v in n.items():
#     #     return k + '_leader', v + '_leader'
#
# it = map(func, listvar)
# print(list(it))
#
# it = map(lambda n: n['name'] + '_leader', listvar)
# print(list(it))

# 第三题
# shares={
#    	'IBM':36.6,
#    	'Lenovo':23.2,
#   	'oldboy':21.2,
#     'ocean':10.2,
# 	}
# lst = [11,12,13,14,15]
# def func1(n):
#     print('这是n：',n)
#
#     # if shares[n] > 20:
#     #     return True
#     # else:
#     #     return False
#     return shares[n] > 20
#
# it = filter(func1, shares)
# print(list(it))
#
# it = filter(lambda n: shares[n] > 20, shares)
# print(list(it))

# 第四题
# portfolio=[
# 	{'name':'IBM','shares':100,'price':91.1},
# 	{'name':'AAPL','shares':20,'price':54.0},
# 	{'name':'FB','shares':200,'price':21.09},
# 	{'name':'HPQ','shares':35,'price':31.75},
# 	{'name':'YHOO','shares':45,'price':16.35},
# 	{'name':'ACME','shares':75,'price':115.65}
# ]
# a小题
# def func(n):
#     print(n)
#     return n['shares'] * n['price']
#
# it = map(func, portfolio)
# print(tuple(it))
# # for i in it:
# #     print(i)
#
# print(0.1 + 0.2)  # 小数的计算偏差

# it = map(lambda n: n['shares'] * n['price'], portfolio)
# print(list(it))

# b小题
# def func(n):
#     print(n)
#     return n['price'] > 100
#
# it = filter(func, portfolio)
# print(list(it))

# it = filter(lambda n: n['price'] > 100, portfolio)
# print(list(it))

# 第五题
listvar = [
    {'sales_volumn': 0},
    {'sales_volumn': 108},
    {'sales_volumn': 337},
    {'sales_volumn': 475},
    {'sales_volumn': 396},
    {'sales_volumn': 172},
    {'sales_volumn': 9},
    {'sales_volumn': 58},
    {'sales_volumn': 272},
    {'sales_volumn': 456},
    {'sales_volumn': 440},
    {'sales_volumn': 239}
]

# def func(n):
#     return n['sales_volumn']
#
#
# it = sorted(listvar, key=func)  # 默认从小到大排序
# it1 = sorted(listvar, key=func, reverse=True)  # 加个参数reverse=True，变成从大到小排序
# print(list(it))
# print(list(it1))

# it = sorted(listvar, key=lambda n: n['sales_volumn'])
# print(list(it))
# it1 = sorted(listvar, key=lambda n: n['sales_volumn'], reverse=True)
# print(list(it1))


# 后5题
# 第一题
# dic = {'x': 'A', 'y': 'B', 'z': 'C'}
# print([k + '=' + v for k, v in dic.items()])
# print(['%s=%s' % (k, v) for k, v in dic.items()])

# 第二题
# lst = ["ADDD","dddDD","DDaa","sss"]
# print([i.lower() for i in lst])
# print([i.upper() for i in lst])

# 第三题
# print([(x, y) for x in range(6) for y in range(6) if x % 2 == 0 and y % 2 == 1])
# print([(x, y) for x in range(0, 6, 2) for y in range(1, 6, 2)])
# li = []
# for x in range(6):
# 	for y in range(6):
# 		if x % 2 == 0 and y % 2 == 1:
# 			li.append((x, y))
# print(li)

# 第四题
# print(['%d*%d=%d' % (j, i, i*j) for i in range(1, 10) for j in range(1, i+1)])
# 一行代码实现99乘法表
# print("\n".join("\t".join(["%s*%s=%s" %(y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)))

# 第五题
# M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# N = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
# 效果一
# print([M[i][j] * N[i][j] for i in range(len(M)) for j in range(len(M[i]))])

# for i in range(len(M)):
#     # print(M[i])
#     for j in range(len(M[i])):
#         print(M[i][j] * N[i][j])

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
# 效果二
# print([[M[i][j] * N[i][j] for j in range(len(M[i]))] for i in range(len(M))])
lst = []
for i in range(len(M)):
    li = []
    for j in range(len(M[i])):
        li.append(M[i][j] * N[i][j])
    lst.append(li)
print(lst)


