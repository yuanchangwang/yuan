# ### 闭包函数
"""
内函数使用了外函数的局部变量,
并且外函数把内函数返回出来的过程叫做闭包
这个内函数叫做闭包函数

# 闭包函数的语法:
def outer():
	a = 5
	def inner():
		print(a)
	return inner

# 对比正常的局部变量
# 局部变量的生命周期最短,在调用结束之后,立即释放.
def func():
	a = 5
	print(a)
func()
print(a)
	
"""

# (1) 闭包函数的定义
def haojie_family():
	father = "王健林"
	def haojie_say():
		print("我老爸%s说了,先定一个小目标,比如赚他一个亿" % (father))
	return haojie_say

func = haojie_family()
# func = haojie_say
func()

# (2) 闭包函数的特点(升级)
'''
闭包的特点:
    内函数使用了外函数的局部变量,外函数的局部变量与内函数发生绑定,延长该变量的生命周期
    (实际内存给它存储了这个值,暂时不释放)
'''
def liupeng_family():
	jiejie = "马蓉"
	meimei = "马诺"
	money = 1000
	
	def jiejie_hobby():
		nonlocal money
		money -= 600
		print("姐姐%s喜欢花钱,买名牌包包,手表,彩电,冰箱,电脑,洗衣机,热水器,家里的钱还剩下%s" % (jiejie,money))
		return money
		
	def meimei_hobby():
		nonlocal money
		money -= 300
		print("妹妹%s喜欢花钱,买LV,香奈儿,倩碧,雅诗兰黛,大宝,六神花露水,肥皂,雕牌洗衣粉,洗涤剂,家里的钱还剩下%s" % (meimei,money))
		return money

	def big_manager():
		return (jiejie_hobby,meimei_hobby)
	
	return big_manager

func = liupeng_family()
# func = big_manager
print(func,type(func))
# func() = big_manager()
tup = func()
print(tup,type(tup))
"""
(
<function liupeng_family.<locals>.jiejie_hobby at 0x000001FF43910F28>,
<function liupeng_family.<locals>.meimei_hobby at 0x000001FF43947048>
 ) 
 <class 'tuple'>
"""

# 调用姐姐
# jiejie = tup[0]
# jiejie()

res1 = tup[0]()
print(res1)
# 调用妹妹
# meimei = tup[1]
# meimei()

res2 = tup[1]()
print(res2)



















































