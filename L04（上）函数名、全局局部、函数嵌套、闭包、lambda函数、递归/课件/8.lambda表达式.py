# ### 匿名函数 lambda表达式
"""
lambda表达式 : 用一句话来表达只具有返回值的函数,简单,方便,直截了当
# 语法:
lambda 参数 :  返回值 

"""

# (1) 无参数的lambda 表达式
def func():
	return "今天新来的女生真漂亮"

func = lambda : "今天新来的女生真漂亮"
res = func()
print(res)


# (2) 有参数的lambda 表达式
def func(n):
	return type(n)

func = lambda n : type(n)
print(   func(10)   ) #print(   type(n)   )


# (3) 带有条件判断的lambda 表达式
def func(n):
	if n % 2 == 0:
		return "偶数"
	else:
		return "奇数"

"""
# 三目运算符: 同一时间可以操作三个值

真区间 if 条件表达式 else 假区间
如果条件表达式成立   走真区间里面的内容
如果条件表达式不成立 走假区间里面的内容
"""

func  =   lambda n   :    "偶数"  if n % 2 == 0 else "奇数"
res = func(16)
print(res)

# 返回较大值
def func(n,m):
	if n>m:
		return n
	else:
		return m
		
func = lambda n,m : n  if n>m else  m
print(   func(40,50)  )























