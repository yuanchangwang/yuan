# ### 字典的相关函数

# 增  
dictvar = {"a":1,"b":2}
dictvar["c"] = 3
print(dictvar)

#fromkeys()  使用一组键和默认值创建字典 (不常用 赋初始值)
listvar = ['a','b','c']
res = {}.fromkeys(listvar,None)
res = {}.fromkeys(listvar,[1,2])

print(res)
"""
a,b,c 中的值 是三个不同变量指向同一个空间的地址值
print(res['a'] is res['b'])
res['a'].append(3)
print(res['b'])
"""

# 删   
#pop()       通过键去删除键值对 (若没有该键可设置默认值,预防报错)
dictvar = {"top":"程咬金","middle":"甄姬","bottom":"鲁班七号"}
res = dictvar.pop("top")
print(res)
print(dictvar)
# pop可以在第二个参数上指定默认值,预防不存在改键时报错
res = dictvar.pop("ppoiiiiuiuiuiiiuiui","对不起,改键不存在")
print(res)

#popitem()   删除最后一个键值对 
dictvar = {"top":"程咬金","middle":"甄姬","bottom":"鲁班七号"}
res= dictvar.popitem()
print(res)
print(dictvar)

#clear()  清空字典
dictvar = {"top":"程咬金","middle":"甄姬","bottom":"鲁班七号"}
dictvar.clear()
print(dictvar)

# 改
#update() 批量更新(有该键就更新,没该键就添加)
dictvar = {"top":"程咬金","middle":"甄姬","bottom":"鲁班七号"}
# 写法一
dictvar.update({'top':111,"jungle":"盘古"}) # 在括号里面写字典数据 (一个字典即可)
# 写法二
dictvar.update(a=1,b=2)  #(在括号里面写关键字参数,是多个)
print(dictvar)

# 查
#get()    通过键获取值(若没有该键可设置默认值,预防报错)
dictvar = {"top":"程咬金","middle":"甄姬","bottom":"鲁班七号"}
res = dictvar.get("top123")
# 如果这个键不存在,可以指定默认值, 如果不写第二个参数值,默认返回None
# res = dictvar.get("top123","对不起,该键不存在")
# res = dictvar['top']
print(res)

#keys()   将字典的键组成新的可迭代对象
dictvar = {"top":"程咬金","middle":"甄姬","bottom":"鲁班七号"}
res = dictvar.keys()
print(res)
for i in dictvar.keys():
	print(i)

for i in dictvar:
	print(i)

#values() 将字典中的值组成新的可迭代对象
dictvar = {"top":"程咬金","middle":"甄姬","bottom":"鲁班七号"}
res = dictvar.values()
print(res)
for i in res:	
	print(i)
	
#items()  将字典的键值对凑成一个个元组,组成新的可迭代对象 
res = dictvar.items()
print(res)
for i in res:	
	print(i)
'''
('top', '程咬金')
('middle', '甄姬')
('bottom', '鲁班七号')
'''
for a,b in res:
	print(a,b)



































