# ### 函数的参数
"""
参数:
(1)形参:形式参数 (在函数的定义处)
(2)实参:实际参数 (在函数的调用处)

形式参数种类: 普通(位置)参数 默认参数 普通收集参数 命名关键字参数 关键字收集参数
实际参数种类: 普通(位置)实参 关键字实参

形参和实参数量要一一对应
"""
# (1)普通形参
# 函数的定义处
# hang 和 lie 就是形参: 普通(位置)形参
def star(hang,lie):
	i = 0 
	while i<hang:
		j = 0
		while j<lie:
			print("*",end="")
			j+=1
			
		print()
		i+=1
# 函数的调用处 10,10 就是实际参数: 普通实参
star(10,10)
# star()

# (2)默认形参
print("<==>")
# hang 和 lie 就是形参: 默认形参 带有默认值
def star(hang=10,lie=10):
	i = 0 
	while i<hang:
		j = 0
		while j<lie:
			print("*",end="")
			j+=1
			
		print()
		i+=1
# 函数的调用处
"""
给与实际参数时候,用自己的
没给与实际参数时,用默认形参的
"""

# 没有参数,使用默认形参所指代的值
# star()
# 一个参数: 默认hang = 1 ,lie = 10
# star(1)
# 两个参数: hang = 4 lie =5
# star(4,5)


# (3) 普通形参 + 默认形参
print("<==33+=>")
# hang 普通形参  lie 默认形参
'''
# *******如果普通形参 + 默认形参都存在的情况下, 优先顺序,普通形参要跟在默认形参的前面;
'''
# 函数的定义处
def star(hang,lie=10):
	i = 0 
	while i<hang:
		j = 0
		while j<lie:
			print("*",end="")
			j+=1
			
		print()
		i+=1
		
# 函数的调用处
# 不写参数不行,因为hang没有默认值
# star()  error

# 写1个参数 hang = 4 lie  =10
# star(4)

# 写2个参数
# star(3,3)

print("<===123>")
# (4)关键字实参
# 函数的定义处
def star(hang,lie=10):
	i = 0 
	while i<hang:
		j = 0
		while j<lie:
			print("*",end="")
			j+=1
			
		print()
		i+=1
		
# 函数的调用处
# lie = 13 是关键字实参
star(3,lie=13)
# hang = 3 ,lie = 5 是关键字实参
star(hang = 3,lie =5)
# 如果是关键字实参,顺序可以颠倒
star(lie = 2,hang=3)
# 如果定义时,是普通形参 ,调用时,是关键字实参调用,那么跟在这个普通形参后面的所有参数,都需要使用关键字实参
def star(hang,a1,a2,lie=10):
	i = 0 
	while i<hang:
		j = 0
		while j<lie:
			print("*",end="")
			j+=1
			
		print()
		i+=1
# 函数的调用处
# star(1,a1= 1,a2 = 3,lie = 18)
star(1,lie=3,a1 = 4,a2=8)








