---
typora-root-url: assets
---
### -python的认知
```
89年开发的语言,创始人范罗苏姆(Guido van Rossum),别称:龟叔(Guido). 
python具有非常多并且强大的第三方库,使得程序开发起来得心应手. Python程序员的信仰:人生苦短,我用python!

(1)版本:
python2x:原码不规范,重复较多
python3x:原码清晰,简单
	
(2)编译型与解释型语言区别:
	编译型:一次性,把所有代码编译成机器能识别的二进制,在运行
		代表语言:c,c++
		优点: 执行速度块
		缺点: 开发速度慢,调试周期长
		
	解释型:代码从上到下一行一行解释并运行 
		代表语言:python,php
		优点: 开发效率快,调试周期短
		缺点: 执行速度相对慢
	*python语言可以直接在linux和windows跨平台使用.

(3)python的解释器:
    (1)Cpython(官方推荐)
    	转化成c语言能识别的二进制码
    (2)Jpython
    	转化成java语言能识别的二进制码
    (3)其他语言解释器
    	把python转化成其他语言能识别的二进制码
    (4)PyPy
    	将所有代码一次性编译成二进制码,加快执行效率(模仿编译型语言的一款python解释器)

```

### -注释: 就是对代码的解释 方便大家阅读代码
```
(1)注释的分类
(2)注释的注意点
(3)注释的排错性
```

### -变量:可以改变的量,实际具体指的是内存中的一块存储空间
```
(1)关于变量的含义
(2)变量的声明
(3)变量的命名
(4)变量的交换

*常量就是不可改变的量,python当中没有明确定义常量的关键字,所以约定俗成把变量名大写就是常量,表示不可改变
```
### -python的六大标准数据类型
```
(1)Number   数字类型(int  float  bool  complex)
(2)String	字符串类型
(3)List		列表类型
(4)Tuple	元组类型
(5)Set		集合类型
(6)Dict		字典类型

->(1)Number 	数字类型分类
int :    		整数类型    (正整数[各种进制] 负整数 0)
float:   		浮点数类型  (1普通小数 2科学计数法表示的小数 例:a = 3e-5  #3e-05 )
bool:    		布尔值类型  (真True和假False)
complex: 		复数类型    (声明复数的2种方法) (复数用作于科学计算中,表示高精度的数据,科学家会使用)	
```


### -自动类型转换

```
当2个不同类型的数据进行运算的时候,默认向更高精度转换
数据类型精度从低到高:bool int float complex
```
### -强制类型转换

```
-->Number 部分
int :     整型   浮点型 布尔类型  纯数字字符串
float:    整型   浮点型 布尔类型  纯数字字符串
complex:  整型   浮点型 布尔类型  纯数字字符串  复数
bool: 	  ( 容器类型数据  /  Number类型数据 都可以 )
```
```
-->容器类型部分
str:	  ( 容器类型数据  /  Number类型数据 都可以 )
list:  	  字符串 列表 元组 集合 字典
tuple: 	  字符串 列表 元组 集合 字典
set:   	  字符串 列表 元组 集合 字典  (注意:相同的值,只会保留一份)
dict:	  使用 二级列表 或 二级元组   (二级集合语法上不错,但是无序,不建议使用)
```
### -python运算符

```
(1)算数运算符:  + - * / // % **
(2)比较运算符:  > < >= <= == !=   
(3)赋值运算符:  = += -= *= /= //= %= **=
(4)成员运算符:  in 和 not in (针对于容器型数据)
(5)身份运算符:  is 和 is not (检测两个数据在内存当中是否是同一个值)  
(6)逻辑运算符:  and or not
(7)位运算符:    & | ~ ^ << >>
```

### 在同一文件(模块)里,变量存储的缓存机制 (仅对python3.x版本负责 了解)


```
-->Number 部分
1.对于整型而言，-5~正无穷范围内的相同值 id一致
2.对于浮点数而言，非负数范围内的相同值 id一致
3.布尔值而言,值相同情况下，id一致
4.复数的id标识都不相同(在 实数+虚数 这样的结构中)
```

```
-->容器类型部分
5.字符串而言，字符串值相同情况下，id一致
6.列表，元组，字典，集合无论什么情况 id标识都不同(但空元组的id标识一样)
```
### 不同文件(模块)里,部分数据驻留小数据池中 (仅对python3.x版本负责 了解)
```
python提前在内存中创建了-5 ~ 256 范围的整数,驻留在了内存的一块区域.
如果是不同文件(模块)的两个变量,并在此范围具有了相同的值,
那么id一致.

小数据池只针对：int ,string,bool,以及空元祖(),None关键字   有效
```
```
对于字符串来说:
(1)字符串的长度为0或者1，默认驻留小数据池
```

![1](.\1.png)

```
(2)字符串的长度>1,且只含有大小写字母，数字，下划线时，默认驻留小数据池
```

![11](.\2.png)

```
(3)用乘法得到的字符串，分两种情况。
1)乘数为1时:
无论什么字符串 * 1 , 都默认驻留小数据池
2)乘数大于1时:
乘数大于1，仅包含数字，字母，下划线时会被缓存，但字符串长度不能大于20
```

![8](/8.png)

```
### 指定驻留 ###
from sys import intern
a = intern('大帅锅&*^^1234'*10)
b = intern('大帅锅&*^^1234'*10)
print(a is b)
#可以指定任意字符串加入到小数据池中,无论声明多少个变量,只要此值相同,都指向同一个地址空间
```

![9](/9.png)
```
*无论是缓存机制还是小数据池的驻留机制,都是为了节省内存空间,提升代码效率
```

![7](/7.jpg)