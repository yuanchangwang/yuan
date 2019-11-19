# ### 字符串相关函数
# *capitalize 字符串首字母大写 

strvar = "this is a dog"
res = strvar.capitalize()
print(res)

# *title 每个单词的首字母大写 (非字母隔开的单词)
strvar = "this is123a dog"
res = strvar.title()
print(res)

# *upper 将所有字母变成大写

strvar = "A C c d"
res = strvar.upper() 
print(res)

# *lower 将所有字母变成小写
res = strvar.lower()
print(res)

# *swapcase 大小写互换  
res = strvar.swapcase()
print(res)

# *count 统计字符串中某个元素的数量 
strvar = "aa bbccfsdfkjak"
res = strvar.count("a")
print(res)


# *find 查找某个字符串第一次出现的索引位置 
'''find('字符串',开始位置,结束位置) 结束位置取不到,取到之前的一个值'''
print("<====>")
strvar = "oh Father this is My Favarate boY"
res = strvar.find("F")    # 3
res = strvar.find("F",4)  # 21
res = strvar.find("F",10,20)
res = strvar.find("aa")
print(res)
# *index 与 find 功能相同 find找不到返回-1,index找不到数据直接报错
# res = strvar.index("aa")  # 推荐使用find


# *startswith 判断是否以某个字符或字符串为开头 
'''startswith和endswith 用法是一样的 都是如下参数('字符串',开始位置,结束位置) 要么返回True 要么返回False'''
strvar = "oh Father this is My Favarate boY"
res= strvar.startswith("oh")
res = strvar.startswith("thi",10) # True
res = strvar.startswith("thi",10,12)
print(res)

# *endswith 判断是否以某个字符或字符串结尾 
res = strvar.endswith("boY")
res = strvar.endswith("bo",-4,-1) #  bo
print(res)

# *****split 按某字符将字符串分割成列表(默认从左到右按空格分割)
strvar = "you can you up no can no bb"
res = strvar.split()
strvar = "you=can=you=up=no=can=no=bb"
res = strvar.split("=",2) # 第二个参数是分割几次 (从左向右)
print(res)
# rsplit 从右向左分割
res = strvar.rsplit("=",1) # (从右向左)
print(res) # 返回列表

# *****join  按某字符将列表拼接成字符串(容器类型都可)
listvar  =  ['you', 'can',"a","basestring"]
res = "*".join(listvar)
print(res)  # 返回字符串



# *replace 替换字符串(第三个参数选择替换的次数)
strvar = "可爱的小狼狗喜欢吃肉,有没有,有没有,还有没有"
res  = strvar.replace("有没有","真没有")
print(res)
# 第三个参数为替换的次数
res = strvar.replace("有没有","真没有",1)
print(res)


# *isdecimal 检测字符串是否以数字组成  必须是纯数字
res = "11323"
res = "1132....3"
print(res.isdecimal())

# *len 计算容器类型长度
res = len("aabbcc")
print(res)

# *center 填充字符串,原字符居中 (默认填充空格)
strvar = "你好"
res = strvar.center(10,"*") #center(填充的个数,填充的字符)
print(res)

# *strip  默认去掉首尾两边的空白符 
strvar = "\r sdf   \t \n"
print(strvar)
res = strvar.strip()
print(res)















