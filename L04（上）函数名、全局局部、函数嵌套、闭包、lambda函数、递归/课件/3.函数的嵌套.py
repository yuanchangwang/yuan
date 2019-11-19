# ### 函数的嵌套
"""
python中允许函数嵌套,嵌套在外层的是外函数,嵌套在里层的是内函数
"""


def func1():
	
	a = 10
	def func2():
		print(a)
		
	func2()
	
		
func1()
# func2()
# (1)内部函数可以直接在函数外部调用么    不行
# (2)调用外部函数后,内部函数可以在函数外部调用吗  不行
# (3)内部函数可以在函数内部调用吗        可以
# (4)内部函数在函数内部调用时,是否有先后顺序 有

print("<===>")
# 定义一个三层嵌套函数,最外层的是outer 第二层是inner ,第三层是smaller,调用smaller
def outer():
	a = 90
	def inner():
		# a = 91
		def smaller():
			print(a)
			print(id)
		smaller()

	inner()
	
outer()


"""
#找寻变量的调用顺序采用LEGB原则(即就近原则)
B —— Builtin(Python)；Python内置模块的命名空间      (内建作用域)
G —— Global(module)； 函数外部所在的命名空间        (全局作用域)
E —— Enclosing function locals；外部嵌套函数的作用域(嵌套作用域)
L —— Local(function)；当前函数内的作用域            (局部作用域)
依据就近原则,从下往上 从里向外 依次寻找
"""
a01 = 10
def func():
	a01 = 20
	del a01
	# 除非不定义,一旦定义过一次局部变量,删除后,会默认认为找不到,报错
	print(a01)
func()












