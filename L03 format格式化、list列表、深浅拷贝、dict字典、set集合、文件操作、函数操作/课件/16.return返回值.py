# ### return 返回值
"""
(1) return + 数据类型 :    将这个数据弹到函数的调用处,后面除了可以接六大标准数据类型之外,还可以返回类 对象 函数 等;默认返回None
(2) 函数当中,执行完return 之后,函数立刻终止,意味着函数里 , 跟在return后面的代码不执行
"""

# (1) 把数据返回到函数的调用处
def func():
	# return 1
	# return "aaabb"
	return [1,2,3,4]

# 这个地方是调用处 函数名()
res = func()  # 相当于 res = 1
print(res)

# (2) 函数的返回值不是必须的,按照需求来,如果不写return 返回值,默认返回None
def func():
	print(1234566)
	
res = func()
print(res)

# 打印1234567 和 自定义的return 之间没有半毛钱关系,返回值是自定义的;
res  = print(1234567)
print(res)

# (3) 写一个计算器
def calc(sign,num1,num2):
	if sign == "+":
		res = num1 + num2
	elif sign == "-":
		res = num1 - num2
	elif sign == "*":
		res = num1 * num2 
	elif sign == "/":
		if num2 == 0:
			return "抱歉,大兄弟,这个算不了"
		res = num1 / num2
	else:
		return "你是外星来的小baby么"
	
	return res
	
res = calc("_",5,1)
print(res)













