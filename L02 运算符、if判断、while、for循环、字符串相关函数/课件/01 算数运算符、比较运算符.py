# ### 运算符


# (1)算数运算符:  + - * / // % **
var1 = 10
var2 = 7
# +
res = var1 + var2
print(res)

# -
res = var1 -var2
print(res) # 3

#*
res = var1 * var2
print(res) # 70

#/ 最后的结果一定是小数
res = 14 / 7
print(res)  #

# // 地板除 整除之后的数
res = 14 // 7
# 如果被除数 或者 除数是一个小数,那么结果后面加一个.0
res = 14.3 // 7
print(res)

# %
res = 8 % 3  # 正常取余数
res = -8 % 3 #-2 + 3 = 1
res = 8 % -3 #2 + (-3) = -1
res = -8 % -5 #-3果两者符号都是符号 那么直接取余数跟上一个负号
print(res)

# **
res = 3 ** 2
res = 2 ** 4
print(res)


# (2)比较运算符:  > < >= <= == != 
"""返回一个布尔类型的值 True False"""
# >
var1 = 5
var2 = 3
res = var1 > var2
print(res)

# <
res = var1 < var2
print(res)

# >=
res = var1 >= var2
res = 5>=5   #满足一个条件即可 方返回真
print(res)

# <=
res = var1 <= var2
res = 5<=5  #满足一个条件即可 方返回真
print(res)

# ==
res = var1 == var2
print(res)
"""
# 额外注意
if var1 == var2:
	print(123)
if var1 = var2: # 赋值运算
	print(345)

0 0.0 0j False '' () [] set() dict() None
"""

# !=
res = var1 != var2
print(res)
















