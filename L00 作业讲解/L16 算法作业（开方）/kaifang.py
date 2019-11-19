import math


def kai_fang(digit, bit_num):
	"""
	求保留指定小数位数的数的开方值，时间复杂度为 O(N),空间复杂度为 O(1)
	:param digit: 要开方的数
	:param bit_num: 保留的小数位
	:return: 开方值
	"""
	digit = float(digit)
	bit_num = int(bit_num)

	if 0 > digit:
		return '负数是没有开方值'

	# 确定整数部分
	int_part = 0  # 整数部分先定义为0
	# math  # alt + enter  快捷导入函数
	# 向上取整的原因： 比如1.1 ，如果直接int强转就变成1，那循环出来的i最大只能取到1，那就计算不到1.1
	for i in range(math.ceil(digit) + 1):
		if digit == i * i:  # 如果能开方的整数就直接返回结果
			return i
		if digit < i * i:  # 比如5， 2的平方小于5,3的平方大于5，所以我们的整数部分就是2
			int_part = i - 1
			break

	result = int_part  # 先把整数部分给到最后的结果

	# 确定小数部分
	for i in range(1, bit_num+2):
		temp = math.pow(10, -i)  # x的y次方   10的-i次方
		for j in range(1, 11):
			temp2 = result + temp * j
			# if digit == temp2 * temp2:
			# 	return temp2
			if abs(digit - temp2 * temp2) < 0.000001:  # 浮点数的数据偏移，会导致精度问题
				return temp2
			if digit < temp2 * temp2:
				result += temp * (j-1)
				break

	return round(result, bit_num)  # round(数值，保留的小数位)



if __name__ == '__main__':
	while 1:
		digit = input('请输入你要开方的数：').strip()
		bit_num = input('请输入你要保留的小数位数：').strip()
		print(kai_fang(digit, bit_num))

# print(0.1*0.1)

# print(9.9)
# print(0.01)
# print(99.9 - 90)
# print(99.9 - 90.9 == 9)
# print(99.9 - 90 == 9.9)


