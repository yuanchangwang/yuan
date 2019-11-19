# ### 集合的相关操作 作用:交差并补
set1 = {"周星驰","周杰伦","周润发","王文"}
set2 = {"王健林","王思聪","王宝强","王文"}
#intersection() 交集 
res = set1.intersection(set2)
print(res)
res = set1 & set2
print(res)

#difference()   差集 
res = set1.difference(set2)
print(res)
res = set2.difference(set1)
print(res)
res = set1 - set2
print(res)
  
#union()  并集    
res = set1.union(set2)
print(res)
res = set1 | set2
print(res)
     
#symmetric_difference() 对称差集 (补集情况涵盖在其中)
res = set1.symmetric_difference(set2)
print(res)

res = set1 ^ set2
print(res)

#issubset()   判断是否是子集 (真子集:子集元素一定少于父集,完全被包含在其中)
set_father = {"周星驰","周杰伦","周润发","王文"}
set_son  = {"周杰伦","周润发"}
res = set_son.issubset(set_father)
print(res)

res = set_son < set_father
print(res)

# 这个情况下,两个集合完全一样,分不清子父关系,不是真子集
set_father = {"周星驰","周杰伦","周润发","王文"}
set_son  = {"周星驰","周杰伦","周润发","王文"}
res = set_son <=  set_father
print(res)

#issuperset() 判断是否是父集
set_father = {"周星驰","周杰伦","周润发","王文"}
set_son  = {"周星驰","周杰伦"}
res = set_father.issuperset(set_son)
print(res)
res = set_father > set_son
print(res)

set_father = {"周星驰","周杰伦","周润发","王文"}
set_son  = {"周星驰","周杰伦","周润发","王文"}
res = set_father >= set_son
print(res)

#isdisjoint() 检测两集合是否不相交  不相交 True  相交False
set_father = {"周星驰","周杰伦","周润发","王文"}
set_son  = {"周星驰","周杰伦"}
res = set_father.isdisjoint(set_son)
print(res)

# ### 集合的相关函数
# 增 
#add()    向集合中添加数据
setvar = {"刘浩杰","徐信信","何伟福","林志远"}
setvar.add("胡斌")
print(setvar)

#update() 迭代着增加
setvar = {"刘浩杰","徐信信","何伟福","林志远"}
lst = ['胡家豪',"胡启超"]
setvar.update(lst) #把列表当中的元素一个一个拿出来放进集合中,需要时可迭代性数据

setvar = {"刘浩杰","徐信信","何伟福","林志远"}
strvar = "abcd"
setvar.update(strvar) 
print(setvar)

# 删
#clear()  清空集合
setvar = {"刘浩杰","徐信信","何伟福","林志远"}
setvar.clear()
print(setvar)

#pop()    随机删除集合中的一个数据
setvar = {"刘浩杰","徐信信","何伟福","林志远"}
res = setvar.pop()
print(res)
print(setvar)

#remove()  删除集合中指定的值(不存在则报错)
setvar = {"刘浩杰","徐信信","何伟福","林志远"}
setvar.remove("徐信信")
print(setvar)
# setvar.remove("徐信信1")

#discard() 删除集合中指定的值(不存在的不删除 推荐使用)
setvar = {"刘浩杰","徐信信","何伟福","林志远"}
setvar.discard("何伟福121211212") # 如果这个值不存在,就不删除,也不报错
print(setvar)


# ### 冰冻集合
'''
#frozenset 可强转容器类型数据变为冰冻集合
冰冻集合一旦创建,不能在进行任何修改,只能做交叉并补操作
'''
# 定义一个空冰冻集合
fz = frozenset()
print(fz,type(fz))

fz1 = frozenset([1,"2",3,4])
fz2 = frozenset("7892")
print(fz1,fz2)

# 并冻集合只能做交叉并补
res = fz1 & fz2
print(res)
# fz1.add(4) error 没有增加或删除操作






























