# ### nonlocal
"""
nonlocal 专门用来修饰[局部变量] 符合LEGB原则
(1)用来修改当前作用域上一层的[局部变量]
(2)如果上一层没有,继续向上寻找
(3)直到再也找不到了,直接报错
"""

#(1)用来修改当前作用域上一层的[局部变量]
def outer():
	a = 1
	def inner():
		nonlocal a
		a += 2
		print(a)
	inner()
outer()

#(2)如果上一层没有,继续向上寻找
def outer():
	a = 20
	def inner():
		a = 10
		def smaller():
			nonlocal a
			a+=2
			print(a) #12
		smaller()
		print(a)     #12
	inner()
	print(a)         #20
outer()


# (3)直到再也找不到了,直接报错
a = 80  # 全局变量 nonlocal不能修饰
def outer():
	# a = 10
	def inner():
		def smaller():
			nonlocal a
			a+=2
			print(a) #12
		smaller()
	inner()
outer()






































