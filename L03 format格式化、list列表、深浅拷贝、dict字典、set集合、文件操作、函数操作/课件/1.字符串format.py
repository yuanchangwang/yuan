# ###字符串的格式化 format
"""
(1)顺序传参
(2)索引传参
(3)关键字传参
(4)容器类型传参(列表和元组)

{} 相当于占位符
"""

# (1) 顺序传参
strvar = "{}向{}开了一枪,饮弹而亡"
res = strvar.format("钟立文","刘鹏")
print(res)

# (2) 索引传参
strvar = "{1}给{0}一个大大的拥抱,幸福温暖"
res = strvar.format("郑慢","林志源")
print(res)

# (3) 关键字传参
strvar = "{who1}向{who2}进行扫射,浑身都是弹孔"
res = strvar.format(who1="中灵芝",who2="戴明雪")
print(res)


# (4) 容器类型传参
# (1)
strvar = "{0[2]}给了{1[0]}抛了一个媚眼,鼻血直冒3000多尺"
res = strvar.format(["钟立文","赵成","胡斌"],("徐欣欣","胡启超"))
print(res)

# (2) format 格式化时, 要注意如果是字典,不要加引号.
strvar = "{group2[0]}给{group1[xxx]}抛了一个媚眼,鼻血直冒3万尺"
res = strvar.format(group1 = {"xxx":"徐欣欣","hqc":"胡启超"},group2=["何伟福","刘鹏"])
print(res)































