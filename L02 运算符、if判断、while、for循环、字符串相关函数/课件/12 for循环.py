# ### for 循环 特指用于遍历容器类型数据
# 遍历 循环 迭代 都是一个意思 就是把所有的数据一个一个拿出来的过程
setvar = {"a","b","c","d"}

# while循环有局限性,不能遍历无序容器数据
'''
i = 0
length = len(setvar)
while i<=length:
	print(setvar[i])
	i+=1
'''
# for 循环应用而生
'''
for i in 可迭代性数据:
把可迭代性数据中的值一个一个拿出啦赋值给i
到最后没有值可以拿了,循环终止.
'''
# 遍历字符串
strvar = "今天我最棒"
for i in strvar:
	print(i)

# 遍历列表
listvar = [1,2,3,4,5]
for i in listvar:
	print(i)

# 遍历元组
print("<==>")
tuplevar = (6,7,8,7)
for i in tuplevar:
	print(i)
# 遍历集合
for i in setvar:
	print(i)

# 遍历字典
# 在遍历字典的时,默认遍历的是键,不是值
dictvar = {'a':1,'b':2,'c':3}
for i in dictvar:
	print(i)

# 二级容器
lst = [1,2,3,(4,5,6)]
# res = lst[-1]
# res = res[-1]
# print(res,"<22>")
print(lst[-1][-1],"<33>")
# 二级列表
listvar = [4,5,6,[77,88]]

# 二级元组
tuplevar = (1,2,3,(5,6,7))

# 二级字典
dic = {"a":1,"b":{"c":1,"d":2}}
print(dic["b"]["d"],"<=33==>")

# 二级集合 : 集合中的数据必须是可哈希的数据(不可变的数据)
set1 = {1,2,3,4,(1,2,3)}

# 四级容器
lst = [1,2,3,4, [5,6,(11,123,{"c":22,"f":33},34),7,8] ]
# 找出33
res = lst[-1][2][-2]["f"]
print(res,"<======333=====>")

# 变量的解包操作
a,b = 1,2
c,d = [5,6]
print(a,b,c,d,"<444>")

# 遍历等长的二级容器,(里面的元素是容器数据,容器里面的元素个数相同)
listvar =[ ["王健林","王思聪"], ["马云","马化腾"],["王宝强","马蓉"]]
# a,b = ["王健林","王思聪"]  # 变量的解包操作
for a,b in listvar:
	print(a,b)

# 不等长的二级容器 (老老实实一层一层遍历)
listvar =[ ["王健林","王思聪"], ["马云","马化腾"],["王宝强"]]
for i in listvar:
	for j in i:
		print(j)
		

# range的用法  返回一个可迭代的对象
'''
range(start,end,step)
start 代表开始值
end   代表结束值 但是高位取不到,取到之前的一个值
step  步长
'''
# 只有一个参数的情况:
for i in range(8): # 0 ~7
	print(i)
# 有2个参数的情况
for i in range(5,8):	# 5 6 7
	print(i)

# 有3个参数逇情况   (正序)
for i in range(1,11,3):# 
	print(i)
print("<==>")
for i in range(9,0,-1):
	print(i)

# 用for 来 改写99乘法表(作业)



