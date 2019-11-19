# ### 函数名的使用
# python中的函数可以像变量一样,动态创建,销毁,当参数传递,作为值返回,叫第一类对象.其他语言功能有限
# 1.函数名是个特殊的变量,可以当做变量赋值
def func():
	print("最近深圳暴雨死了不少人")
	
res = 4+3j
res = func
# res()  =  func()
# 把func当成变量赋值给res ,此刻res也成为了函数,调用函数需要在res后面加上()
res()

# del 是删除关键字
del res
# res()
# func()


# 2.函数名可以作为容器类型数据的元素
def func1():
	print(11)
def func2():
	print(22)
def func3():
	print(33)


lst = [func1,func2,func3]
print(lst)
# 循环调用列表当中的每一个函数
for i in lst:
	i()


# 3.函数名可以作为函数的参数
print("<===>")
def func1(func):
	# 函数的调用处
	res = func()
	print(res)

# 函数的定义处
def func2():
	return 123
	
func1(func2)

'''
定义处就是def 声明的地方
调用处就是func()加上括号的地方
'''
# 4.函数名可作为函数的返回值
def func1(func2):
	# 返回到函数的调用处
	return func2
def func2():
	return 456

# 参数func2
res = func1(func2)
# print(res)
# print(res())



# ### 自定义函数文档
'''
__doc__ 魔术属性:获取函数自定义文档的相关内容 函数.__doc__
'''
def eat_big_chang(something):
	'''
	功能:吃大肠方法
	参数:盛放的器皿
	返回值:一个状态
	'''
	print("把肠子盘成一圈放在%s里" % (something))
	print("找肠子头放嘴里")
	print("使劲嗦")
	print("满意的放下场子头")
	return "好吃"


eat_big_chang("盆里")
print(eat_big_chang.__doc__)
































