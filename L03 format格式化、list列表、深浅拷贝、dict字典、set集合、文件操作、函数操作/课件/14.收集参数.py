# ### 收集参数
'''
(1) 普通收集参数
(2) 关键字收集参数
'''

# (1) 普通收集参数 (任意长度都可以接收)
'''
def func(*args):
	pass
*args 就是普通收集参数 : * + 参数名字(名字自定义,一般约定俗成叫做args => arguments 参数的意思)

用途:专门用于收集多余的没人要的普通实参,都放到一个元组当中收集
'''
# 函数的定义处 定义好收集参数args
def func(a,b,c,*args):
	print(a,b,c)
	print(args)

# 函数的调用处
func(1,2,3,4,5,56,6,7)


# 计算任意长度的累加和
def mysum(*args):
	total = 0
	for i in args:
		total += i
	print(total)
	
mysum(1,2,3,4,4,5)


# 关键字收集参数
'''
def func(**kwargs):
	pass
**kwargs 就是关键字收集参数 : ** + 参数名字 (名字自定义,一般约定俗成叫做kwargs => keyword arguments 参数的意思)	

用途:专门用于收集多余的没人要的关键字实参,都放到一个字典当中收集	
'''
# 函数的定义处,定义关键字收集参数
def myfunc(a,b,c,**kwargs):
	print(a,b,c)
	print(kwargs)
# 函数的调用处
myfunc(a=1,b=3,c=5,d=10,e=21)



# 拼接任意长度的字符串
"""
班长:{} 刘浩杰
班花:{} 徐欣欣 + \n
"""

def myfunc2(**kwargs):
	dictvar = {"monitor":"班长","classflower":"班花"}
	str1 = ''
	str2 = ''
	# print(kwargs)  # kwargs 是字典 {'monitor': '刘浩杰', 'classflower': '徐欣欣', 'ly': '龙阳'}
	for k,v in kwargs.items():
		if k in dictvar:
			# print(k) # monitor clasflower
			str1 += dictvar[k] + ':' + v  + '\n'
			# str1 += "班长" + ":" + 刘浩杰 + '\n'
		else:
			# 如果不符合条件,将抠脚大汉名字拼接在一起
			str2 += v + ' '
			
	print(str1,"今天眉开眼笑")
	print(str2,"抠脚大汉,惘闻生痰")
myfunc2(monitor = "刘浩杰",classflower="徐欣欣",ly="龙阳",hb="胡兵")




















