import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
	exp = [math.exp(i) for i in scores]
	sum_exp = sum(exp)
	probabilities = [round(i / sum_exp, 4) for i in exp]
	return probabilities