# ###多项分支 (多选一)
'''
# 语法:
if 条件表达式1:
	code1
	...
elif 条件表达式2:
	code1
	...
elif 条件表达式3:
	code1
	...
else:
	code1
	...
默认从上到下
如果条件表达式1成立则执行代码块,否则向下执行
判断elif中的表达式2是否成立,如果ok执行代码块,否则继续向下执行表达式3,
依次类推,如果没有一个条件表达式成立,
最后执行else区间里面的内容

如果有一个条件满足,就执行该区间的内容,剩下的所有条件都不执行了

elif 可以是1个,可以是多个,
else 只能是1个,或者没有		
'''
youfang = False
youche = False
youkuang = True
youyanzhi = False
youtili = False

# 双项分支
if youfang == True:
	print("我就嫁给你")
else:
	print("你是个好人")

# 多项分支
if youfang == True:
	print("我就嫁给我")
elif youche == True:
	print("我就嫁给你")
elif youkuang == True:
	print("我就嫁给我")
elif youyanzhi == True:
	print("我就嫁给我")
elif youtili == True:
	print("我就嫁给我")
else:
	print("兄die,你还是做2路汽车走吧,我们不合适,是我配不上你")



# ###巢状分支 (单项分支,双项分支 多项分支的嵌套使用)
youfang = True
youche = True
youkuang = True
youyanzhi = True
youtili = False
if youfang == True:
	if youche == True:
		if youkuang == True:
			if youyanzhi == True:
				if  youtili == True:
					print("我就嫁给你1")
				else:
					print("恭喜你,成为我的1号备好 2")
		else:
			print("把你的矿变成钱,整型之后练身材,我就会看上你了3")
else:
	print("我们不合适4")



#出题 height
#女生找对象
	# 男生在1米~1.5米之间 小强 你在哪里?
	# 男生在1.5~1.7米之间 没有安全感~
	# 男生 1.7~ 1.8米之间 帅哥 留个电话
	# 男生 1.8~2米之间 帅哥 你建议多一个女朋友吗

height = float(input("请输入您的身高:"))
# print(height,type(height))
""""""
# height = 1.83
# (1)python特有语法
"""
if 1<=height<=1.5:
	print("小强 你在哪里?")
elif 1.5< height<=1.7:
	print("没有安全感~")
elif 1.7<height<=1.8:
	print("帅哥 留个电话")
elif 1.8<height<=2:
	print("帅哥 你建议多一个女朋友吗")
else:
	print("没有改身高的外星人类")
"""
# (2)通用写法
if height>=1 and height<=1.5:
	print("小强 你在哪里?")
elif height>1.5 and height<=1.7:
	print("没有安全感~")
elif height>1.7 and height<=1.8:
	print("帅哥 留个电话")
elif height>1.8 and height<=2:
	print("帅哥 你建议多一个女朋友吗")
	
else:
	print("没有改身高的外星人类")


























