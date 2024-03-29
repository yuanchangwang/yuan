### -递归函数
```
递归的定义:自己调用自己就是递归函数 有去有回
递归注意事项:
	函数调用的过程就是开辟栈帧和释放栈帧的过程,调用时开辟栈帧空间,结束时释放
	(言外之意不结束这层栈帧不释放)
	递归每次调用都会开辟一个栈帧,如果递归的层数过多,不建议使用,容易内存溢出
	每次开辟的栈帧空间,代码必须全部执行完毕之后才释放空间,在回到上一个栈帧执行没结束的代码
	如果使用递归 , 需要给与一个跳出的条件,不能无限递归
```

### -尾递归(了解)
```
尾递归:
在函数返回的时候，调用其本身，并且，return语句不包含表达式。
(简单来说是递归函数,且只调用自己的非表达式)
尾递归意义:
使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况.(需要Python解释器支持)

```
### -内存栈区堆区(了解内容)
```
单独讲栈堆是数据结构
    栈:后进先出的一种数据结构
    堆:排序后的一种树状数据结构
    
栈区堆区是内存空间
    栈区:按照后进先出的数据结构(栈),无论创建或销毁都是自动为数据分配内存,释放内存
(系统自动做的)
    堆区:按照排序后的树状数据结构(堆),可优先取出必要数据,无论创建或销毁都是手动分配内存,释放内存(程序员手动做的)
    --内存中的栈区 : 自动分配 自动释放
    --内存中的堆区 : 手动分配 手动释放

运行程序时在内存中执行,会因为数据类型的不同而在内存的不同区域运行
因不同语言对内存划分的机制不一,但大体来讲,有如下四大区域

--栈区: 分配局部变量空间.
--堆区: 是用于手动分配程序员申请的内存空间.
--静态区(全局栈区): 分配静态变量，全局变量空间.
--代码区(只读区,常量区): 分配常量和程序代码空间的. 
	
栈区 堆区 静态区 代码区 都是内存中的一段空间
```

### -匿名函数
```
lambda 函数表达式:  只实现一些简单的函数功能,但是写法非常简便
```
### -迭代器
```
迭代器:能被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator  迭代器是对象)
特征:迭代器会生成惰性序列,它通过计算把值依次的返回,一边循环一边计算而不是一次性得到所有数据
优点:需要数据的时候,一次取一个,可以大大节省内存空间.而不是一股脑的把所有数据放进内存.

--Iterable可迭代的  Iterator迭代器
惰性序列:没有一次性的把所有数据都放在序列中,而是遍历一个放一个,这样的序列

range 是 可迭代对象
range 和 迭代器 能够产生惰性序列 
```
### -高阶函数

```
高阶函数:能够把函数当成参数传递的就是高阶函数

# map
map(func,iterable)
功能:
	把iterable里面所有数据 一一的放进到func这个函数中进行操作 ,把结果扔进迭代器
参数:
	func  内置或自定义函数
	iterable 具有可迭代性的数据 ([迭代器],[容器类型的数据],[range对象])
返回值: 
	返回最后的迭代器


# reduce
reduce(func,iterable)
功能:   
    先把iterable里面的前2个数据拿到func函数当中进行运算,得到结果,
    在把计算的结果和iterable中的第三个数据拿到func里面进行运算,
    依次类推 ,直到iterable里面的所有数据都拿完为止,程序结束
参数:
	func     内置或自定义函数
	iterable 具有可迭代性的数据 ([迭代器],[容器类型的数据],[range对象])
返回值: 
	计算的最后结果


# sorted 
sorted(iterable,reverse=False,key=函数)
功能:  
	对数据进行排序
参数: 
    iterable  : 具有可迭代性的数据(迭代器,容器类型数据,可迭代对象)
    reverse   : 是否反转 默认为False 代表正序, 改成True 为倒序
    key       : 指定函数 内置或自定义函数
返回值:
	返回排序后的数据


# filter
filter(func,iterable)
功能:
    用来过滤的,如果func函数中返回True , 会将这个值保留到迭代器中
    如果func函数中返回False , 会将此值舍弃不保留
参数:
    func : 自定义函数
    iterable : 具有可迭代性的数据(迭代器,容器类型数据,可迭代对象)
返回值: 
	返回处理后的迭代器

```