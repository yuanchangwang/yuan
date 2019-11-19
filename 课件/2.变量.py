# ### 1.变量: 可以改变的量就是变量  具体指的是内存的一块空间
rujia_305 = "王文"
print(rujia_305)
rujia_305 = "张三"
print(rujia_305)


# ### 2.变量的声明
# 方法一
a = 1
b = 2
print(a)
print(b)

# 方法二
a,b = 3,4
print(a,b)

# 方法三
a = b = 5
print(a,b)


# ### 3.变量的命名
"""
          变量的命名
字母数字下划线,首字符不能为数字
严格区分大小写,且不能使用关键字
变量命名有意义,且不能使用中文哦
"""
print("<====>")
yuyu_999234sdfsdf = 1
# 234234_sdfsd = 90
_234sdfsd = 80
abc = 55
ABC = 66
print(abc)
print(ABC)
print(yuyu_999234sdfsdf)

# import 引入 keyword 模块名
import keyword
# 模块名.属性 kwlist 可以打印出所有的关键字
res = keyword.kwlist
print(res)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
# 命名要有意义
car = "本田"
abcd = "本田"

# 用中文命名变量语法上允许,但严禁使用
"""
utf-8 国际通过编码格式(可变长的unicode编码集) 一个中文占用三个字节 一个英文占用1个字节
gbk   国标编码集 (中国标准的编码集)           一个中文占用两个字节 一个英文占用1个字节
"""
中文 = "周杰伦"
print(中文)



# ### 4.变量的交换
# 通用的交换写法
a = 11
b = 12
tmp = a
a = b
b = tmp
print(a,b)

# python 写法
a = 11
b = 12
a,b = b,a
print(a,b)

















