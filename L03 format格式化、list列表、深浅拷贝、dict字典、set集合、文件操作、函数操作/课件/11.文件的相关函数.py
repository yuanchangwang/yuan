# ### 文件操作的相关函数
# 刷新缓冲区 flush
    # 当文件关闭的时候自动刷新缓冲区
    # 当整个程序运行结束的时候自动刷新缓冲区
    # 当缓冲区写满了  会自动刷新缓冲区
    # 手动刷新缓冲区
	
fp = open("0414_7.txt",mode="w+",encoding="utf-8")
fp.write("我在测试close操作")
# 立刻把缓冲区里面的内容刷入文件当中,缓冲区只是临时存储数据用的.不会一直存数据
fp.flush() 
# while True:
	# pass
fp.close()


# (1)readline()     功能: 读取一行文件内容
"""
readline(字符个数) 单位读的时字符的个数
如果当前字符个数 > 实际个数 那就只读当前行
如果当前字符个数 < 实际个数 那就按照给与的当前个数读取 
"""
''''''
# 读出所有行数 每一行都读
fp = open("0414_8.txt",mode = "r+",encoding="utf-8")
res = fp.readline(3)
# res = fp.readline()
# 判断res是不是为空,如果不是空,则进去打印该字符串
while res:
	print(res)
	# 在继续向下读取一行
	res = fp.readline() # 读到最后是一个'' bool('') => False


# (2)readlines()    功能：将文件中的内容按照换行读取到列表当中
'''
listvar = []
with open("0414_8.txt",mode = "r+",encoding="utf-8") as fp:
	
	res = fp.readlines()
	# 过滤数据
	for i in res:
		# 过滤两边的空白符
		res = i.strip()
		# 把过滤好的数据直接插入到列表当中
		listvar.append(res)
print(listvar)
'''


# (3)writelines()   功能：将内容是字符串的可迭代性数据写入文件中 参数:内容为字符串类型的可迭代数据
'''
with open("0414_9.txt",mode="w+",encoding="utf-8") as fp:
	# strvar = "123456"
	# strvar = ["aaa",'bbb','ccc']
	# res = str([1,2,3,4,5])
	fp.writelines(res)
'''

# (4)truncate()     功能: 把要截取的字符串提取出来,然后清空内容将提取的字符串重新写入文件中 (字节)
'''
with open("0414_9.txt",mode="r+",encoding="utf-8") as fp:
	fp.truncate(5)
'''


#readable()	    功能: 判断文件对象是否可读
# writable ()	    功能: 判断文件对象是否可写
"""
fp = open("0414_9.txt",mode="w",encoding="utf-8")
res1 = fp.readable()
res2 = fp.writable()
print(res1,res2)

# 文件对象具有可迭代性  
# 遍历fp对象 和 readline一行一行读取的操作是一样的.
for i in fp:
	print(i)
"""





