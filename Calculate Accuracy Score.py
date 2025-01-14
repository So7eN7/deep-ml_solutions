import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
    acc = np.sum(y_true == y_pred, axis=0) / len(y_true)
    return acc 