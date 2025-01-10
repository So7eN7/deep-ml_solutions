import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros((n, 1))
	for i in range(iterations):
		pred = X @ theta
		loss = pred - y.reshape(-1, 1)
		update = alpha * (X.T @ loss) / m
		theta -= update
	return np.round(theta, 4)