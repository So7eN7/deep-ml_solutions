import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y = np.array(y)
	X_trans = X.T
	theta = np.linalg.inv(X_trans.dot(X)).dot(X_trans).dot(y).round().tolist() 
	return theta