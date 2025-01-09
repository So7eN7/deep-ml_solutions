def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	col = len(matrix)
	row = len(matrix[0])
	result = matrix
	for i in range(row):
		for j in range(col):
			result[i][j] = scalar * result[i][j]
	return result

'''
Better solution by the website itself
'''

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    return [[element * scalar for element in row] for row in matrix]
