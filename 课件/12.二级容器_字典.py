# ### 二级容器: 外面是一个容器类型的数据,里面的元素还是一个容器类型数据
listvar = [1,2,3,(4,5,6)] # 二级容器

# 二级列表
listvar = [1,2,3,[4,5,6]]
print(listvar)

# 二级元组
tup = (3,5,(7,8,9))
print(tup)

# 二级集合  (只能存放元组)
setvar = {1,2,3,(11,22,33)}
print(setvar)

# 二级字典
dictvar = {'a':{'c':333},'b':2}
# 取出333
print(dictvar['a']['c'])

# 四级容器
container = [1,2,3,(4,5,6,{"a":1,"b":[7,8,9]}),90]
# 取出9
res = container[-2][-1]["b"][-1]
print(res)

# 等长的二级容器  
'''
(1) 里面每个元素都是容器类型数据
(2) 每个容器类型数据的元素个数都相同
'''
container = [(1,2,3),[4,5,6]]


# ### 字典的强制类型转换 
'''
需要等长的二级容器,而且每个容器里面的元素只能是两个
'''

#(1) 外面是列表,里面是列表或元组或字符串
listvar = [["a",1],("b",2),"c123"] # 字符串慎用 如果值是多个,有局限性
listvar = [["a",1],("b",2)]  # 推荐 ***
res = dict(listvar)
print(res)

#(2) 外面是元组,里面是列表元组或字符串
tuplevar = (["c",11],("d",23))  # 推荐 ***
res = dict(tuplevar)
print(res)

# 例外:如果往列表或者元组容器放集合,语法上不报错,但情况出乎意料,达不到想要效果
container  = dict([{"a",1},{"b",2}]) # 不推荐使用
print(container)

#(3) 外面是集合,里面是元组或字符串
setvar = {('a',1),('b',2),"c3"} # 必须放入不可变数据,即可哈希
res = dict(setvar)
print(res)


"""
int() float() bool() complex()
str() list() tuple() set() dict()
这些函数在进行强转时,都默认转化成当前的数据类型
用这样的方式也可以初始化一个变量
"""
res = int()
res = list()
print(res)






















