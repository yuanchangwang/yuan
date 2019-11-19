# ### 容器类型数据 list tuple
""" list 可获取,可修改,有序"""
# (1)定义一个空列表
listvar = []
print(listvar,type(listvar))

#正向索引  0   1    2   3     4
listvar = [13,3.14,True,6-2j,"我是大帅哥"]
#反向索引  -5  -4   -3  -2     -1

# (2)获取列表当中的值
res = listvar[4]  # 正向索引
res = listvar[-1] # 反向索引
print(res)

# 通用 => 想要获取列表最后一个元素值 需要通过len函数
# len 用来获取容器类型数据的元素个数(长度)
# 5 - 1 => 4
res = len(listvar)-1

# print(listvar[res])  
print(listvar[len(listvar)-1])

# (3)修改列表当中的值
listvar[3] = "和抚慰"
listvar[-4] = "比养生"
print(listvar)


# ### tuple
""" 可获取,不可修改,有序"""
'''
证明是一个元组的根本特征是逗号,声明一个空元组,可以直接使用(),(1) 表明一个整型
'''
# (1) 声明一个空元组 
tuplevar = ()
print(tuplevar,type(tuplevar))
tuplevar = (1,2,3,4)
print(tuplevar,type(tuplevar))
tuplevar = (1,)
print(tuplevar,type(tuplevar))
tuplevar = 1,2,3
print(tuplevar,type(tuplevar))


# 获取最后一个值
#正向索引    0  1   2
tuplevar = ("a","b",False)
#逆向索引    -3  -2  -1
res = tuplevar[-1]
#或者 res = tuplevar[len(tuplevar)-1]
print(res)

# (2)元组不可修改
# tuplevar[-1] = True error


# ### str 字符串和元组几乎一模一样,只不过每一个元素都是字符
'''可获取,不可修改,有序'''
#         0 1  2 3 45 6 7 8
strvar = "瞅你一眼,浑身哆嗦"
#         -9-8-7-6-5-4-3-2-1
# (1)获取字符串中的一字
res = strvar[2]
res = strvar[-7]
print(res)

# (2) 字符串无法修改
# strvar[-1] = "!" error










