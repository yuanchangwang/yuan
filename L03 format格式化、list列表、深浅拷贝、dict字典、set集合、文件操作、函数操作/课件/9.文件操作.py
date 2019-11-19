# ### 文件操作
'''
fp = open("打开的文件",mode="模式选择",encoding="编码集")
open 函数 返回一个文件io对象 (别名:文件句柄)
i => input   输入
o => output  输出
'''

"""
把大象放冰箱里:需要三部
	打开冰箱门
	把大象塞进去
	关上冰箱门
"""


# (1)写入文件内容 
# 打开文件
fp = open("0414.txt",mode="w",encoding="utf-8") # 打开冰箱门
# 写入内容
fp.write("我就是那个大象") # 把大象塞进去
# 关闭文件
fp.close() # 关上冰箱门

# (2)读取文件内容
# 打开文件
fp = open("0414.txt",mode="r",encoding="utf-8") # 打开冰箱门
# 读取内容
res = fp.read()  #把大象拿出来
# 关闭文件
fp.close()       # 关上冰箱门

print(res)


# b bytes模式 (二进制的字节流)
'''
一堆字符放在一起 是字符串
一堆字节放在一起 是字节流
字节流用来传输数据,用来保存数据
'''
# 在ascii编码字符前加上b ,代表二进制字节流,其他所有字符都不能这样加(比如中文是不行的)
strvar = b'123'
print(strvar,type(strvar)) #b'123' <class 'bytes'>

# 使用encode 和 decode 来吧中文转化成二进制字节流
# encode 把中文变成字节流 (编码)
strvar = "奔跑吧兄嘚"
res = strvar.encode("utf-8")
print(res)
# decode 把字节流变成中文 (解码)
strvar = res.decode("utf-8")
print(strvar)


# 复制图片 
# 实际上就是把图片中的二进制字节流拷贝出来,放到另外一个文件当中.
'''二进制字节流模式,不要指定编码集utf-8'''
# [读取]文件里面的内容
fp = open("集合.png",mode="rb")
res = fp.read()
fp.close()

# [写入]另外一个文件中
fp = open("集合2.png",mode="wb")
res = fp.write(res)
fp.close()




























