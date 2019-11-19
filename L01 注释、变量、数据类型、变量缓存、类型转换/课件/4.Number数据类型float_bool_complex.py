# ### float bool  complex

# (1)float 浮点型 小数
# 表达一
floatvar  =  3.15
print(floatvar,type(floatvar))

# 表达二
floatvar = 5.35e-3
floatvar = 7.34e5
print(floatvar,type(floatvar))

# (2)bool 布尔类型 (True 真的 False 假的)
boolvar = True
boolvar = False  
print(boolvar,type(boolvar))

# (3)complex 复数类型
"""
复数:
实数 + 虚数
j:如果一个数的平方等于-1,那么这个数就是j
科学家认为有,表达一个高精度的类型
"""
# 1.方式一
complexvar = 3+4j
print(complexvar,type(complexvar))

# 2.方式二 complex(实数,虚数)
complexvar = complex(-5,-2)
print(complexvar)