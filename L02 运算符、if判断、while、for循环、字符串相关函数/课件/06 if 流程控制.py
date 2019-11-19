# ### 流程控制:
'''
流程:代码执行的过程
流程控制:对代码执行过程的管控

流程控制三大结构:
	(1)顺序结构:从上到下,代码依次执行
	(2)分支结构: 一共4个
	(3)循环结构:while for

分支结构:
(1) 单项分支
(2) 双项分支
(3) 多项分支
(4) 巢状分支
'''

# (1)单项分支
"""
# 语法
if 条件表达式:
	code1
	code2
	...
	...
如果条件表达式成立,则执行if代码块中的内容
"""
zhaocheng = "高富帅"
if zhaocheng == "高富帅123":
	print("我就嫁给你")

# (2)双项分支 (二选一)
"""
if 条件表达式:
	code1
	code2
	...
else:
	code1
	code2
	...
如果条件表达式成立 则执行if当中代码块的内容
如果条件表达式不成立 则执行else当中代码块的内容
if下面的代码块叫做 真区间
else 下面你的代码块叫做 假区间
"""

# xuxinxin = "美女"
xuxinxin = "绿巨人"
if xuxinxin == "美女":
	print("追求她")
	print("给她买雅诗兰黛")
	print("给她买倩碧")
	print("给他买兰蔻")
	print("给她买香奈儿")
	print("给他买包,因为包治百病")
else:
	print("你是个好人...")


# input 等待用户输入内容   * input  接受到的所有数据都是字符串类型
# res = input("欢迎观临,你叫什么名字呀")
# print(res)

'''
	提示用户输入用户名和密码:
	如果用户名是admin , 并且密码是000 , 
	提示用户恭喜你,登陆成功
	否则提示用户名或密码错误
'''
username = input("请输入您的用户名:")
pwd = input("请输入您的密码:")
# print(username,type(username))
# print(pwd,type(pwd))
if username == "admin" and pwd == "000":
	print("恭喜你,登录成功")
else:
	print('抱歉,您的用户名或密码错误')










