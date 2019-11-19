# 第一题
# class Person(object):
#     animal = '高级动物'
#     soul = '有灵魂'
#     language = '语言'
#
#     def __init__(self, country, name, sex, age, stature):
#         self.country = country
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.stature = stature
#
#     def eat(self):
#         print('%s在吃饭' % self.name)
#
#     def sleep(self):
#         print('睡觉')
#
#     def work(self):
#         print('工作')
#
#
# p1 = Person('中国', 'alex', '未知', 42, 175)
# p2 = Person('美国', '武大', '男', 35, 160)
# p3 = Person('中国', '老王', '未知', 38, 183)
# p4 = Person(p1.country, p2.name, p3.sex, p2.age, p3.stature)
#
# p1.eat()
# p2.eat()
# p3.eat()
#
# print(p1.animal)
# print(p2.soul)
# print(p3.language)


# 第二题
# class Person(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def hobby(self):
#         print('%s, %s岁, %s, 上山去砍材' % (self.name, self.age, self.sex))
#         print('%s, %s岁, %s, 开车去东北' % (self.name, self.age, self.sex))
#         print('%s, %s岁, %s, 最爱大保健' % (self.name, self.age, self.sex))
#
#
# p1 = Person('小明', 10, '男')
# p2 = Person('老李', 90, '男')
# p1.hobby()
# p2.hobby()


# 第三题
# class Game_role(object):
#     def __init__(self, name, ad, hp):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#
#     def attack(self, enemy):
#         print('%s攻击%s,%s掉了%d血,还剩%d血' %
#               (self.name, enemy.name, enemy.name, self.ad, enemy.hp-self.ad))
#
#
# p1 = Game_role('盖伦', 10, 100)
# p2 = Game_role('剑豪', 20, 80)
# p1.attack(p2)
# p2.attack(p1)
#
# print(str(80-10))


# 第四题
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def perimeter(self):  # 计算周长
#         print(math.pi * self.radius * 2)
#
#     def area(self):  # 计算面积
#         print(math.pi * (self.radius * self.radius))
#
#
# p1 = Circle(5)
# p1.perimeter()
# p1.area()

# 第5题
# dic = {p1: 111, Circle: 222}
# print(dic)
# print(dic[p1])
# print(dic[Circle])

# 第七题
# class A:
#     __name = 'alex'
#     def __eat(self):
#         print(111)
#     def func1(self):
#         print(self.__name)
#
# class B(A):
#     def func(self):
#         print(self.__name)

# a = A()
# print(a._name)
# # print(1111, a._A__name)
# b = B()
# print(b._name)
# # b.func()
# a.func1()
# b.func1()

# 第八题
# class StarkConfig(object):
#     def __init__(self,num):
#         self.num = num
#     def changelist(self,request):
#         print(self.num,request)
#
# class RoleConfig(StarkConfig):
#     def changelist(self,request):
#         print('666')
#
# config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
# obj1 = StarkConfig(1)
# obj2 = StarkConfig(2)
# obj3 = RoleConfig(3)
# for item in config_obj_list:
#     print(item.num)
"""
1
2
3
"""

# 第九题
# class StarkConfig(object):
#     def __init__(self,num):
#         self.num = num
#     def changelist(self,request):
#         print(self.num,request)
#
# class RoleConfig(StarkConfig):
#     pass
#
# config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
# # obj1 = StarkConfig(1)
# # obj2 = StarkConfig(2)
# # obj3 = RoleConfig(3)
# for item in config_obj_list:
#     item.changelist(168)
# print(config_obj_list[0].num)
"""
1, 168
2, 168
3, 168
1
"""

# 第十题
# class StarkConfig(object):
#     def __init__(self,num):
#         self.num = num
#     def changelist(self,request):
#         print(self.num,request)
#
# class RoleConfig(StarkConfig):
#     def changelist(self,request):
#         print(666,self.num)
#
# config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
# # obj1 = StarkConfig(1)
# # obj2 = StarkConfig(2)
# # obj3 = RoleConfig(3)
# for item in config_obj_list:
#     item.changelist(168)
"""
1, 168
2, 168
666, 3
"""

# 第十一题
# class StarkConfig(object):
#     def __init__(self,num):
#         self.num = num
#     def changelist(self,request):
#         print(self.num,request)
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#     def changelist(self,request):
#         print(666,self.num)
#
# config_obj_list = [StarkConfig(1),StarkConfig(2),RoleConfig(3)]
# # obj1 = StarkConfig(1)
# # obj2 = StarkConfig(2)
# # obj3 = RoleConfig(3)
# config_obj_list[1].run()
# config_obj_list[2].run()
"""
2, 999
666, 3
"""

# 第十二题
# class StarkConfig(object):
#     def __init__(self,num):
#         self.num = num
#     def changelist(self,request):
#         print(self.num,request)
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#     def changelist(self,request):
#         print(666,self.num)
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#     def register(self,k,v):
#         self._registry[k] = v
#
# site = AdminSite()
# print(len(site._registry))  # 0
# site.register('range',666)
# site.register('shilei',438)
# print(len(site._registry))  # 2
#
# site.register('lyd',StarkConfig(19))
# site.register('yjl',StarkConfig(20))
# site.register('fgz',RoleConfig(33))
# print(len(site._registry))  # 5
# print(site._registry)
"""
{'range': 666, 'shilei': 438, 'lyd': StarkConfig(19), 'yjl': StarkConfig(20), 'gfz': RoleConfig(33)}
"""

# class A:
#     def __init__(self, num):
#         self.num = num
#
# a = A(19)
# print(a)


# 第十三题
# class StarkConfig():
#     def __init__(self,num):
#         self.num = num
#     def changelist(self,request):
#         print(self.num,request)
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#     def changelist(self,request):
#         print(666,self.num)
#
# class AdminSite():
#     def __init__(self):
#         self._registry = {}
#     def register(self,k,v):
#         self._registry[k] = v
#
# site = AdminSite()
# site.register('lyd',StarkConfig(19))
# site.register('yjl',StarkConfig(20))
# site.register('fgz',RoleConfig(33))
# # print(len(site._registry))
# # print(site._registry)
#
# for k,row in site._registry.items():
#     row.changelist(5)
# """
# 19, 5
# 20, 5
# 666, 33
# """
# for k,row in site._registry.items():
#     row.run()
"""
19, 999
20, 999
666, 33
"""

class JustCounter:
	__secretCount = 0
	def count(self):
		self.__secretCount += 1
		print(self.__secretCount)
	def count3():
		print(JustCounter.__secretCount)

class Bars(JustCounter):
	def count2(self):
		print(self.__secretCount)

#  情况一
counter1 = JustCounter()
counter1.count()  # 1     counter1.__secretCount = 0 + 1  ===>  1
counter1.count()  # 2     counter1.__secretCount = 1 + 1  ===>  2
# counter1 改变的是自己空间里的__secretCount，没有修改类空间的__secretCount
# 因为对象无法修改类空间的属性，只能自己创建一个一模一样的属性进行修改

#  情况二
counter2 = Bars()
counter2.count()  # 1
counter2.count()  # 2
# counter2 改变的是自己空间里的__secretCount，没有修改类空间的__secretCount
# 因为对象无法修改类空间的属性，只能自己创建一个一模一样的属性进行修改


#  情况三
JustCounter.count3()  # 0
# 所以类空间的私有属性还是0，没有被修改

"""
对象可以调用类的属性和方法，但是无法修改他，要修改的话其实是在自己的对象空间创建了一个一模一样的属性
（对象空间中有一个类指针，所以可以通过该指针找到类）
类是无法调用对象空间的属性和方法的
"""


