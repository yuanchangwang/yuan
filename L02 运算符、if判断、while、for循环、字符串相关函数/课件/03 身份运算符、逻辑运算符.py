# ### 身份运算符 is | is not 检测两个数据在内存中是否是同一个地址

'''
仅仅限定在3.6版本之前 是变量的缓存 ,
判断一个值在某个范围内存在,就不会再另外创建一个相同的值,为了节省内存空间
3.7之后不再划定范围,只要有一份就缓存
提出小数据池 或者变量缓存是为了提升代码执行的效率,减少内存占用空间
'''
# 整型 -5 ~ 正无穷
var1 = 19
var2 = 19
res = var1 is var2
print(res)

# 浮点型  非负数
var1 = -5.52
var2 = -5.52
res = var1 is not var2
print(res)

# 复数 在实数 + 虚数这样的结构中永远不一样 但如果只有虚数 在值相同情况下一样
var1 = 3+4j
var2 = 3+4j
res = var1 is  var2
var1 = 6j
var2 = 6j
res = var1 is not var2
print(res)

# bool 在布尔值相同的情况下 id一样
var1 = True
var2 = True
res = var1 is var2
print(res)

# 容器类型数据地址判断

# str 字符串而言，字符串值相同情况下，id一致
var1 = "你"
var2 = "你"
print(var1 is var2)


var1 = (1,23)
var2 = (1,23)
print(var1 is var2)
# 空元组例外
var1 = ()
var2 = ()
print(var1 is var2)

# 剩下的容器类型数据无论什么值都不一样
var1 = [1,2]
var2 = [1,2]
print(var1 is not var2)


# ### 逻辑运算符 and or not 
print("<===>")
# and 逻辑与
'''小明写作业:数学和英语都写完叫写完'''
"""***** 全真则真 一假则假"""
res  = True and  True
res = True and False
res = False and True
res = False and False
print(res)

# or  逻辑或
"""妈妈奖励小明:说有一门考及格了,我就给你买布加迪威龙"""
'''***** 全假则假 一真则真'''
res = True or True
res = True or False
res = False or True
res = False or False
print(res)

# not 逻辑非(相当于取反)
res = not True
res = not False
print(res)

# 逻辑短路
"""
一个or或者一个and 情况下
(1)True or something
(2)False and something
"""

print("<===>")
False or print(123)
True and print(456)

# 逻辑优先级
# () > not > and > or 
res = 5 or 6 and 7
res = (5 or 6) and 7 # 5 and 7
res = not (5 or 6) and 7 # not 5 and 7 => False and 7 => False
print(res) # 5 or 7

res = 1<2 and 3>4 or 5<6 # True and False or True => False or True
res = 1<2 and 3>4 or 5>6 and 7<8 or 9>10 # True and False or False and True or False =>False or False or False => False or False => False		
print(res)

# 这种情况特殊,上来直接短路,后面的不用再按照and or 优先级算了 (例外)
res = 5 or 6 and 7 or 8 and 9 or 10
# 如果上来直接是假,不一定结果也是假,要依次向后计算
# False and True or True 


#数据类型判断 isinstance
"""
int float bool complex str list tuple set dict

isinstance(要判断类型的数据,(类型1,类型2,类型3......))
如果在类型元组当中,返回真
如果不在类型元组当中,返回假
"""
intvar  = 15
print(isinstance(intvar,int))
strvar = "789"
print(isinstance(strvar,(int,str,list)))















