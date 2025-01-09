def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'column':
		means = [sum(i) / len(matrix) for i in zip(*matrix)]
	elif mode == 'row':
		means = [sum(i) / len(i) for i in matrix]
	else:
		return -1
	return means
