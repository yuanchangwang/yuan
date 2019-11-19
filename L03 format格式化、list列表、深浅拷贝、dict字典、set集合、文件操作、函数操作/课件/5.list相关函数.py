# ### 列表相关的函数
# (1) append
'''
功能：向列表的末尾添加新的元素
格式：列表.append(值)
返回值：None
注意：新添加的值在列表的末尾，该函数直接操作原有列表
'''

# 增     
# (1) append
listvar = [1,2,3,4,5]
listvar.append(6)
listvar.apppend([12,3])
print(listvar)

# (2) insert()
'''
功能：在指定索引之前插入元素
格式：列表.insert(索引,值)
返回值:None
注意：直接改变原有列表
'''
listvar = [1,2,3,4,5]
listvar.insert(2,7)
print(listvar)

# (3)extend()
'''
功能：迭代追加所有元素
格式：列表.extend(可迭代性数据)
返回值：None
注意：直接改变原有列表
'''
listvar = [1,2,3,4,5]
listvar.extend(("你","好"))
# listvar.extend({'a':1,"b":2}) 语法上允许
print(listvar)

# 删
# (1) pop
'''
功能：通过指定索引删除元素,若没有索引移除最后那个
格式：列表.pop(索引)
返回值：删除的元素
(注意：没有指定索引，默认移除最后一个元素 )
'''
listvar = [1,2,3,4,5]
res = listvar.pop()
print(res) 
print(listvar)
listvar = [1,2,3,4,5]
res = listvar.pop(3) # 指定索引
# res = listvar.pop(33)  删除不存在的报错
print(listvar)

# (2) remove()
'''
功能：通过给予的值来删除,如果多个相同元素,默认删除第一个
格式：列表.remove(值)
返回值：无
(注意：如果有索引的情况推荐使用pop,效率高于remove)
'''
listvar = [1,2,3,4,5]
listvar.remove(4)
print(listvar)


# (3) clear()
'''
功能：清空列表
格式：列表.clear()
返回值：空列表
'''
listvar = [1,2,3,4,5]
listvar.clear()
print(listvar)

# 改查 具体参数列表相关操作
# 列表其他操作 

# (4)index()
'''
功能：获取某个值在列表中的索引
格式：列表.index(值[,start][,end]) # []  表达参数可选项 
返回值：找到返回索引  (找不到报错)
'''
listvar = [1,2,3,4,54,4,90,4,78,78787,7878]
res = listvar.index(3)
# res = listvar.index(99) # 如果索引不存在直接报错
res = listvar.index(4,4) # 5
res = listvar.index(4,6,9) # 指定索引的查找范围,高位取不到
print(res)


# (5)count()
'''
功能：计算某个元素出现的次数
格式：列表.count(值)
返回值：次数
'''
listvar = [1,2,3,4,54,4,90,4,78,78787,7878]
res= listvar.count(4)
print(res)

# (6)sort()
'''
功能：列表排序(默认小到大排序)
格式：列表.sort(reverse=False)                        
返回值：None
注意：直接更改原列表
'''
listvar = [78,12,-3,99]
# 默认从小到大排序 (正序)
listvar.sort()
print(listvar)
# 从大到小排序 用reverse = True (倒叙)
listvar.sort(reverse=True)
print(listvar)

# (7) reverse()  单纯的反转
'''
功能：列表反转操作
格式：列表.reverse()
返回值：None
注意：直接更改原列表
'''
listvar = [78,12,-3,99]
listvar.reverse()
print(listvar)









