# ### 文件操作 (+ 扩展模式)
"""
# (utf-8编码格式下 默认一个中文三个字节 一个英文或符号 占用一个字节)
    #read()		功能: 读取字符的个数(里面的参数代表字符个数)
    #seek()		功能: 调整指针的位置(里面的参数代表字节个数)
    #tell()		功能: 当前光标左侧所有的字节数(返回字节数)
"""
# (1)r+ 可读可写 (先读后写)
fp = open("0414_2.txt",mode="r+",encoding="utf-8")
res = fp.read()
print(res)
fp.write("ffzzz")

# 读取所有字符串
fp.seek(0)
res = fp.read()
print(res)
fp.close()


# (2)r+ 可读可写 (先写后读)
fp = open("0414_1.txt",mode="r+",encoding="utf-8")
# 先把光标移动到文件最后
fp.seek(0,2)
# 在最后追加abcd ,避免覆盖以前原有字符串
fp.write("abcd")
# 把光标移动到文件开头
fp.seek(0)
res = fp.read()
print(res)
fp.close()


# (3)w+ 可读可写 (默认光标在文件的开头)
fp = open("0414_3.txt",mode="w+",encoding="utf-8")
fp.write("今天天气下了雨")

# 可读
fp.seek(0)
res = fp.read()
print(res)
fp.close()

'''
除了r模式不能够自动创建文件之外,w和a都可以
'''
# (4)a+ append 可读可写 (默认光标在文件的结尾) (在写入的时候,只能在末尾强制追加)
fp = open("0414_4.txt",mode="a+",encoding="utf-8")
fp.write("今天晚上要早走")

fp.seek(0)
res = fp.read()
print(res)
fp.close()


# seek read tell
fp = open("0414_5.txt",mode="a+",encoding="utf-8")
# fp.write("123456789")

res = fp.tell() # 返回当前光标左边所有字符的字节
print(res)
fp.seek(4)       # 移动到第四个字节的位置
res = fp.tell()  # 返回当前光标左侧所有的字节数
print(res)

res = fp.read(2) # read可以在括号里面指定读几个[字符]
res = fp.tell()  # 获取当前光标左侧的字节数
print(res)
fp.close()


# 可以使用with 语法 简化操作  可以省去fp.close() 这句代码,实现自动关闭
# with + open(文件操作) as 为open的返回值起别名  fp 就是名称
# 相当于 fp = open() 一样的
with open("0404_6.txt",mode="a+",encoding="utf-8") as fp:
	fp.write("ceshidaima")
	fp.seek(0) # fp.seek(0,2) 移动到文件的末尾
	res= fp.read()
	print(res)
	# fp.close 这句话 with语法自动帮助我们完成


# 简化文件复制操作  open 之间 可以用逗号,隔开 为了简化操作
with open("集合.png",mode="rb") as fp1,open("集合3.png",mode="wb") as fp2:
	res = fp1.read()
	strvar  = fp2.write(res)
	































