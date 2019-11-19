
# 1.有变量name = "aleX leNb" 完成如下操作：
name = "aleX leNb"
# 移除 name 变量对应的值两边的空格,并输出处理结果
# res = name.strip()
# print(res)

# 1)移除name变量左边的"al"并输出处理结果
res = name.lstrip('al')
print(res)

# 2)移除name变量右面的"Nb",并输出处理结果
res = name.rstrip('Nb')
print(res)
name = "aleX leNb"
# 3)移除name变量开头的a"与最后的"b",并输出处理结果
res = name[1:-1]
print(res)
# 4)判断 name 变量是否以 "al" 开头,并输出结果
res = name.startswith('al')
print(res)
# 5)判断name变量是否以"Nb"结尾,并输出结果
res = name.endswith('Nb')
print(res)
# 6)将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
name = "aleX leNb"
res = name.replace('l', 'p')
print(res)
# 7)将name变量对应的值中的第一个"l"替换成"p",并输出结果
res = name.replace('l', 'p', 1)
print(res)
# 8)将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
res = name.split('l')
print(res)
# 9)将name变量对应的值根据第一个"l"分割,并输出结果。
res = name.split('l', 1)
print(res)
name = "aleX leNb"
# 10)将 name 变量对应的值变大写,并输出结果
res = name.upper()
print(res)
# 11)将 name 变量对应的值变小写,并输出结果
res = name.lower()
print(res)
# 12)将name变量对应的值首字母"a"大写,并输出结果
res = name.capitalize()
print(res)
# 13)判断name变量对应的值字母"l"出现几次，并输出结果
res = name.count('l')
print(res)
name = "aleX leNb"
res = len(name)
print(res)
# 14)如果判断name变量对应的值前四位"l"出现几次,并输出结果
res = name[0:4].count('l')
print(res)
# 15)从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
res = name.index('N')
print(res)
# 16)从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1)输出结果
res = name.find('N')
print(res)
# 17)从name变量对应的值中找到"X le"对应的索引,并输出结果
res = name.find('X le')
res = name.index('X le')
print(res, 111)
name = "aleX leNb"
# 18)请输出 name 变量对应的值的第 2 个字符?
res = name[1]
print(res)
# 19)请输出 name 变量对应的值的前 3 个字符?
res = name[0:3]
print(res)
# 20)请输出 name 变量对应的值的后 2 个字符?
res = name[7:]
print(res)
res = name[-2:]
print(res)
# 21)请输出 name 变量对应的值中 "e" 所在索引位置?
res = name.find('e')
print(res)
res = name.index('e')
print(res)
print('======')
for k, v in enumerate(name):
	if v == 'e':
		print(k)
name = "aleX leNb"
# 2.实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:") 用户输入：5+9或3+ 9或5 + 6，然后进行分割再进行计算
# content = input("请输入内容:").strip()
# print(content, type(content))
# res = content.split('+')
# print(res)
# sum = int(res[0].strip()) + int(res[1].strip())
# print(sum)

# 3.升级题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+  13，然后进行分割再进行计算。
# content = input("请输入内容:").strip()
# res = content.split('+')
# print(res, len(res))
# count = 0
# for i in res:
# 	count += int(i)
# print(count)

# 4.计算用户输入的内容中有几个整数（以个位数为单位）。
# 如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla
# content = input("请输入内容：").strip()
# count = 0
# for i in content:
# 	if i.isdigit():  # isalnum 判断是否为数字或者字母,  isalpha 判断是否为字母
# 		count += 1
# print(count)

# 5.等待用户输入数据,检测用户输入内容中是否包含敏感字符？
# 如果存在敏感字符提示"存在敏感字符请重新输入"，
# 并允许用户重新输入打印。
# (敏感字符：小粉嫩,大铁锤)
# li = ['小粉嫩', '大铁锤']
# while 1:
# 	res = input('>>>>').strip()
# 	for i in li:
# 		if i in res:
# 			print('存在敏感字符请重新输入')
# 			break
# 	else:
# 		print('没有敏感字符')
# 		break

# 6.字符串格式化：
# 等待用户输入名字、地点、爱好，根据用户的名字和爱好
# 拼装数据打印：
# 敬爱可亲的xxx，
# 最喜欢在xxx地方xxx
name1 = input('请输入名字:').strip()
id = input('请输入地点:').strip()
hobby = input('请输入爱好:').strip()
print('敬爱可亲的%s，最喜欢在%s地方%s' % (name1, id, hobby))
print('敬爱可亲的{}，最喜欢在{}地方{}'.format(name1, id, hobby))
print('敬爱可亲的{0}，最喜欢在{1}地方{2}'.format(name1, id, hobby))
print('敬爱可亲的{0}，最喜欢在{0}地方{0}'.format(name1))




