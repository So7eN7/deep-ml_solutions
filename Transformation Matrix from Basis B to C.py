import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	B = np.array(B)
	C = np.array(C)
	P = np.dot(np.linalg.inv(C), B)
	P = P.tolist()
	return P