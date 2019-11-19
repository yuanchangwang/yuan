# ### locals 和 globals

# (1)locals()  :返回字典,获取当前作用域的所有内容
"""
    如果在函数里:获取locals()调用之前,该作用域出现的内容
    如果在函数外:获取locals()打印返回值之前,该作用域出现的内容
"""
# (1)所在作用域是全局命名空间,打印res之前的所有获取内容
"""
a = 1
b = 2

def func():
	d = 5
	f = 7

res = locals()
c = 3
print(res)
"""
'''
{
	'__name__': '__main__', 
	'__doc__': '\n    如果在函数里:获取locals()调用之前,该作用域出现的内容\n    如果在函数外:获取locals()打印返回值之前,该作用域出现的内容\n', 
	'__package__': None, 
	'__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001AC593AA208>, 
	'__spec__': None, '__annotations__': {}, 
	'__builtins__': <module 'builtins' (built-in)>, 
	'__file__': 'D:/深圳周末三期/L004/7.py', 
	'__cached__': None, 
	'a': 1, 
	'b': 2
}

'''
# (2)所在作用域是局部命名空间,获取locals() 调用之前所出现的所有局部命名空间内容
"""
c=3
d = 4
def func():
	a = 1
	b = 2
	
	res = locals()
	c = 3
	print(res)
	
f = 5
func()
"""


# (2)globals() :返回字典,获取全局作用域的所有内容
"""
    如果在函数里: 获取globals()调用之前,全局作用域出现的内容
    如果在函数外: 获取globals()打印返回值之前,全局作用域出现的内容
"""
# 1. globals在全局作用域中,只获取globals 打印返回值之前的所有全局空间的内容
'''
a = 1
b = 2
res = globals()
print(res)
c = 3
'''

'''
{
'__name__': '__main__',
'__doc__': '\n    如果在函数里:获取locals()调用之前,该作用域出现的内容\n    如果在函数外:获取locals()打印返回值之前,该作用域出现的内容\n', 
'__package__': None, 
'__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000145B5DBA208>, 
'__spec__': None, '__annotations__': {}, 
'__builtins__': <module 'builtins' (built-in)>, 
'__file__': 'D:/深圳周末三期/L004/7.py', 
'__cached__': None, 
'a': 1, 'b': 2, 'res': {...}}
'''

# 2.globals在局部作用域中,也仍然获取全局空间的所有内容,但是是在globals,打印返回值之前的所有.
"""
c = 13
d = 14
def func():
	a = 11
	b = 12
	res = globals()
	print(res)
f = 19
func()
"""

# 动态创建全局变量 利用globals
'''
globals 返回的是一个系统的全局字典,
键是变量名,值是该标量所指向的值
'''
dic = globals()
dic['wangwen'] = "风流倜傥,高大威猛,威武帅气,万人迷"
print(wangwen)


# 动态创建5个全局变量p1~p5
def func():
	for i in range(1,6):
		dic["p%d" % (i)] = i
		
func()
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)














