# ### 函数的概念
"""
(1)函数的含义:
	功能 (包裹一部分代码 实现某一个功能 达成某一个目的)
(2)函数特点:
	可以反复调用,提高代码的复用性,提高开发效率,便于维护管理

(4)函数命名
"""
# (3) 函数的基本格式
"""
# 语法格式
def 函数名():
	pass	
"""

# 函数的定义
def func():
	print("我就是函数")

# 函数的调用
func()


# 函数的命名:
"""
	      函数的命名
字母数字下划线,首字符不能为数字
严格区分大小写,且不能使用关键字
函数命名又意义,且不能使用中文哦
"""

'''
# 驼峰命名法
(1)大驼峰命名法: MyWorld 每个单词首字符都是大写
(2)小驼峰命名法: myWork  只有第一个单词首字符小写,剩下都大写
函数命名当中不做强制要求,但是对于类名来讲,建议使用大驼峰
函数命名: 一般如下: my_work ,  my_beatiful_girl
'''

# 定义一个函数
def cheng_fa_biao99():
	for i in range(1,10):
		for j in range(1,i+1):
			print("%d*%d=%2d " % (i,j,i*j),end="")
		print()

# 调用函数
cheng_fa_biao99()
cheng_fa_biao99()
cheng_fa_biao99()
cheng_fa_biao99()
cheng_fa_biao99()
cheng_fa_biao99()
cheng_fa_biao99()
cheng_fa_biao99()
















