# ### 深拷贝 与 浅拷贝
'''
a = 10
b = a
a = 20
print(b)

listvar = [1,2,3,4,5]
lst2 = listvar
listvar.append(6)
print(lst2)
print(lst2 is listvar)
'''

# 浅拷贝
# 方法一
listvar = [1,2,3,4,5]
lst2 = listvar.copy()
listvar.append(6)
print(lst2)

# 方法二
# import  引入 copy 模块
import copy
# copy 模块下的copy方法
listvar = [1,2,3,4,5]
lst = copy.copy(listvar)
listvar.append(14)
print(lst)

# 深拷贝
import copy
lst = [
	{"a":{'c':1,'d':3},"b":[5,6,7,8]},	
	4,5	
]
# 浅拷贝只能拷贝列表的一级 , 如果想要拷贝所有层级,需要使用深拷贝
lst2 = copy.deepcopy(lst)
lst[0]['b'].append(9)
print(lst)
print(lst2)





