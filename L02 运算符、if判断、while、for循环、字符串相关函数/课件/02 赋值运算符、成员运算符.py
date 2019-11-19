# 赋值运算符 = += -= *= /= //= %= **=
var1 = 8
var2 = 3
# =
# var1 = var2
# print(var1)

# +=
# var1 += var2 
'''var1 = var1 + var2'''
# print(var1)

# -=
# var1 -= var2
'''var1 = var1 - var2'''
# print(var1)

# *=
# var1 *= var2
# var1 = var1 *var2
# print(var1) 

# /=
# var1 /= var2
# var1 = var / var2
# print(var1)

# //= 地板除运算
# var1 //= var2
# var1 = var1 // var2
# print(var1)

# %= 余运算
# var1 %= var2
# var1 = var1 % var2
# print(var1)

# **= 幂运算
var1 = 4
var1 **= 3
print(var1)



# (4)成员运算符:  in 和 not in (针对于容器型数据)
# str 必须是一个连续的片段
strvar = "如果遇到你是一种错,那我宁愿一错再错"
res = "你" in strvar
res = "遇到"  in strvar
res = "那宁" in strvar
print(res)

# list tuple set 
listvar = ["钟立文","刘鹏","何伟福","龙阳"]
res = "龙阳" not in listvar
setvar = {"戴明雪","郑慢","林志元","中灵芝"}
print(setvar)
res = "郑慢" in setvar
print(res)
tuplevar = ("胡家豪","徐欣欣","胡斌")
res = "徐欣欣" not in tuplevar
print(res)

# dict  成员运算符 判断字典时 判断的是键 不是那个所对应的值
dictvar = {"top":"程咬金","bottom":"甄姬","middle":"嫦娥"}
res = "程咬金" in dictvar
res = "top" not in dictvar
print(res)

















