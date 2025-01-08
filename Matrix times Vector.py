def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	c = []
	if len(a[0]) != len(b):
		return -1
	else:
		for i in a:
			res = 0
			for j in range(len(b)):
				res += i[j] * b[j]
			c.append(res)

	return c
