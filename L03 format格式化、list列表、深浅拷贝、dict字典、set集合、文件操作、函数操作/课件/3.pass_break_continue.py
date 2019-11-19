# ### 关键字的使用 pass / break / continue

# pass 过 起到占位的作用
if 5 == 5:
	pass

# break 只能应用在循环当中 用于终止当前循环
# 打印1~10 遇到5终止循环
i = 1
while i<=10:
	
	if i == 5:
		break
	print(i)
	i+=1

i = 1
while i<=3:
	j = 1
	while j<=3:
		print(i,j)
		if j == 2:
			break  # 终止当前所在的循环
		j+=1
	i+=1


# continue 跳过当前循环,从下一次循环开始
# 打印1~10 不打印5
i = 1
while i<=10:
	
	if i == 5:
		i+=1
		continue
		
	print(i)
	
	i+=1
	
# 打印所有1~100 不含有4的数
# 方法一
i = 1
while i <= 100:
	
	if "4" in  str(i):
		i+=1
		continue
		
	print(i)	
	i+=1
	
# 方法二
print("<==>")
i = 1
while i<=100:
	if i // 10 == 4 or i % 10 == 4:
		i+=1
		continue
		
	print(i)
	i+=1









