# ### 闭包的特点
"""
闭包的特点:
    内函数使用了外函数的局部变量,外函数的局部变量与内函数发生绑定,延长该变量的生命周期
    (实际内存给它存储了这个值,暂时不释放)
"""
def outer(val):
	def inner(num):
		return val + num
	return inner
	
func = outer(10)
# func = inner
res = func(5)
print(res)
"""
# 代码解析:
	func = outer(10)
	val 形参接收到实参值10
	因为内函数使用了外函数的局部变量val,val与内函数发生绑定,延长val的生命周期
	res = func(5)
	num 形参接收到实参值5
	return 10 + 5 => return 15 返回到函数的调用处
	func(5) 是调用处 所以
	res = 15
"""

'''
# 获取闭包函数使用的绑定变量 闭包函数.__closure__  返回单元cell  , cell 里面存的是对应的绑定变量
res = func.__closure__  # 获取到一个元组
res = res[0].cell_contents # res[0] 获取元组当中的第一个值 是一个cell单元 通过单元.cell_contents来获取其中的值,就会知道绑定的变量是谁了. cell_contents是一个属性
print(res,type(res))
# print(res.cell_content)
# (<cell at 0x000001D6DAE17708: int object at 0x000000005EC26D30>,)

'''

# 闭包的意义

# 模拟鼠标点击次数操作
num = 0
def click():
	global num
	num += 1
	return num
res = click()
res = click()
res = click()
# num = 100  恶意串改
res = click()
res = click()
print(res)


# 使用闭包函数重写鼠标点击次数
"""
闭包的意义:
	闭包可以优先使用外函数中的变量,并对闭包中的值起到了封装保护的作用.外部无法访问.
"""
def click():
	x = 0
	def func():
		nonlocal x
		x+=1
		return x
	return func

click  = click()
res = click()
res = click()
res = click()
x = 100
res = click()
res = click()
print(res)

















































