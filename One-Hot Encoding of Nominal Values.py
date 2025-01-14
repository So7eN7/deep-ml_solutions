import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if n_col == None:
		n_col = np.amax(x) + 1
	onehot = np.zeros((x.shape[0], n_col))
	for i in range(x.shape[0]):
		onehot[i, x[i]] = 1
		'''
		more advanced way of doing it via the website solution
		onehot[np.arange(x.shape[0]), x] = 1
		'''
	return onehot

