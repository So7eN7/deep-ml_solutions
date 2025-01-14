import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	scores = scores - np.max(scores) 
	scores = scores - np.log(np.sum(np.exp(scores)))
	return scores