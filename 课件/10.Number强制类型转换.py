# ### 强制类型转换 Number => (int float  bool complex)

var1 = 13
var2 = 99.99
var3 = True
var3_1 = False
var4 = 4+1j
var5 = "123321"
var6 = "你好123"



# 把数据强制转换成整型 int  (整型  浮点型 布尔类型  纯数字字符串)
# int
res = int(var2)
print(res)
# True 强转整型是1 False 强转整型是0
res = int(var3)
res = int(var3_1)
print(res)
res = int(var5)
print(res,type(res))
# res = int(var6)  :error
# print(res,type(res))  :error



# float   (整型   浮点型 布尔类型  纯数字字符串)
res = float(var1)
res = float(var3) # 加上.0 成为小数
res = float(var3_1) # 0.0
# res = float(var4)  #can't convert complex to float
res = float(var5)  #123321.0
print(res)


# complex  (整型   浮点型 布尔类型  纯数字字符串  复数)
res = complex(var1)  # 13 + 0j
res = complex(var2)   #(99.99+0j)
res = complex(var3)  #(1+0j)
res = complex(var3_1) #0j
res = complex(var5)   #(123321+0j)
print(res)



# bool ( 容器类型数据  /  Number类型数据 都可以,要么True要么False)
res = bool(var6)
res = bool(var4)
res = bool([1,2,3])
print("<!!!>")
print(res)
"""  *****五颗星 *****
布尔类型为假的十种情况:
0,0.0,False,0j,"",[],(),set(),{},None
None 是系统的一个关键字 表示空的,什么也没有,一般做初始值
"""
res = None
print(res,type(res))




















