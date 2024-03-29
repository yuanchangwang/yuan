# ### 列表的相关操作
# (1) 列表的拼接
lst1 = [1,2,3]
lst2 = [4,5,6]
res = lst1 + lst2
print(res)

# (2) 列表的重复
lst1 = [7,8,9]
res = lst1 * 3
print(res)

# (3) 列表的切片
'''
语法 => 列表[::]  完整格式：[开始索引:结束索引:间隔值]
	(1)[开始索引:]  从开始索引截取到列表的最后
	(2)[:结束索引]  从开头截取到结束索引之前(结束索引-1)
	(3)[开始索引:结束索引]  从开始索引截取到结束索引之前(结束索引-1)
	(4)[开始索引:结束索引:间隔值]  从开始索引截取到结束索引之前按照指定的间隔截取列表元素值
	(5)[:]或[::]  截取所有列表
'''
listvar = ["陈出兵","刘豪杰","郑慢","龙阳","戴明雪","林志远","赵成","刘鹏","徐欣欣"]
# (1)[开始索引:]  从开始索引截取到列表的最后
res= listvar[1:]
print(res)

# (2)[:结束索引]  从开头截取到结束索引之前(结束索引-1)
res = listvar[:4]
print(res)

# (3)[开始索引:结束索引]  从开始索引截取到结束索引之前(结束索引-1)
res = listvar[4:6]
print(res)

# (4)[开始索引:结束索引:间隔值]  从开始索引截取到结束索引之前按照指定的间隔截取列表元素值
# 0 3 6 9   先把数字数出来,通过下标找对应值
res = listvar[::3]
print(res)
# 3 5 7 9 
print(listvar[3::2])
# 0 3 6
print(listvar[:5:3])

# 倒叙
# ['徐欣欣', '刘鹏', '赵成', '林志远', '戴明雪', '龙阳', '郑慢', '刘豪杰', '陈出兵']
print(listvar[::-1])
# -2 -4 
print(listvar[-2:-6:-2])

# (4) 列表的获取
#          0          1         2
listvar = ["胡启超","中林志","胡家豪"]
#          -3           -2        -1
res = listvar[2]
print(res)
res = listvar[-1]
print(res)


# (5)列表的修改   ( 可切片 )
listvar = ["胡启超","中林志","胡家豪","徐信息"]
listvar[3] = "123"
print(listvar)
# 如果使用了切片进行修改,右侧必须是可迭代性数据(容器类型数据)
# listvar[2:] = "123"  
listvar[2:] = range(0,4)
print(listvar) 

listvar = ["胡启超","中林志","胡家豪","徐信息"]
# 如果使用了切片,并且指定了第三个参数间隔值,那么截取几个,就放几个,一一对应
listvar[::2] = ("a","b")
print(listvar)
# (6)列表的删除   ( 可切片 )
listvar = ["胡启超","中林志","胡家豪","徐信息"]
del listvar[1]
print(listvar)

# 可以使用切片删除
listvar = ["胡启超","中林志","胡家豪","徐信息"]
del listvar[1:3]
print(listvar)

# 元组当中的一级数据更改不了,但是二级或者多级如果是列表这样的数据可修改
tup = (1,2,3,4,5,[1,2,3,45])
tup[-1][-1] = 54
print(tup)













