# (1)打印十行十列小星星 (用两个循环)


print("<==>")
j = 0
while j<10:

	# 打印一行十个小星星
	i = 0
	while i<10:
		print("*",end="")
		i+=1

	# 控制换行
	print()
	j+=1

# 打印十行十列隔列换色小星星
'''外层行j动一次,里面列i动10次,外层动的慢,里层动的块'''
print("<==>")
j = 0
while j<10:

	# 打印一行十个小星星
	i = 0
	while i<10:
		# 控制打印星星的
		if i % 2 == 0:
			# 控制打印黑星
			print("★",end="")
		else:
			# 控制打印白星
			print("☆",end="")
		i+=1

	# 控制换行
	print()
	j+=1


# 打印十行十列隔行换色小星星
print("<==>")
j = 0
while j<10:

	# 打印一行十个小星星
	i = 0
	while i<10:
		# 控制打印星星的
		if j % 2 == 0:
			# 控制打印黑星
			print("★",end="")
		else:
			# 控制打印白星
			print("☆",end="")
		i+=1

	# 控制换行
	print()
	j+=1
	
	
# 99乘法表
# 方向一
i = 1
while i<=9:

	# 输出99乘法表
	j = 1
	while j<=i:
		print("%d*%d=%2d " % (i,j,i*j),end="")
		j+=1
	
	# 执行换行
	print()
	
	i+=1
# 方向二
print("<==>")
i = 9
while i>=1:


	# 输出99乘法表
	j = 1
	while j<=i:
		print("%d*%d=%2d " % (i,j,i*j),end="")
		j+=1
	
	# 执行换行
	print()


	i-=1

# 100~ 999 找吉利数字 111 222 123 321 888 ...

"""
n = 567
n // 100 => 5
n // 10 % 10 =>6
n % 10 => 7
"""
print(567 % 10)
# 方法一
i = 100
while i<=999:
	#百位
	baiwei = i // 100
	#十位
	shiwei = i // 10 % 10
	#个位
	gewei = i % 10 
	
	if shiwei == gewei  and shiwei == baiwei :
		print(i)
	
	# 123 456
	if shiwei == gewei - 1 and shiwei == baiwei +1:
		print(i)
	
	# 654 987
	if shiwei == gewei+1 and shiwei == baiwei -1:
		print(i)
	
	
	i+=1



# ###百钱买百鸡  公鸡1块钱一只  母鸡 3块钱一只  小鸡5毛钱一只 100块钱 买 100只鸡 有多少种买法(经典题型)
"""
穷举法:一个一个试
a => (1,2)
b => (3,4)
c => (5,6)
a+b+c == 10?

1 3 5 
1 3 6
1 4 5 
1 4 6
2 3 5
2 3 6
2 4 5
2 4 6
x,y,z
x+y+z == 100 and  x + y*3+0.5*z = 100
"""
# x公鸡 y 母鸡 z小鸡
x = 0
while x <=100:

	y = 0
	while y<=33:
	
		z = 0
		while z<= 100:
		
			if (x+y+z == 100) and (x+y*3+0.5*z == 100):
				print(x,y,z)
			z+=1
	
		y+=1

	x+=1


























