# ### 自动类型转换 (针对于Number类型) bool float int complex
'''
当Number不同的数据类型进行运算的时候,默认向更高精度转化
精度从低到高顺序:
	bool -> int -> float ->complex
	True 默认转化是1
	False 默认转化是0
'''
# (1) bool + int
res = True + 89
print(res)

# (2) bool + float
res = True + 55.78
print(res)

# (3) bool + complex
res = False + 2-4j
print(res)

# (4) int  + float
res = 31 + 4.1
print(res)

# (5) int + complex
res = 17 + 4-7j
print(res)

# (6) float + complex
res = 8.12 + 3+5j
print(res)