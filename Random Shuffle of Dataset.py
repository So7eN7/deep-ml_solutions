import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
    if seed:
        np.random.seed(seed)
    index = np.arange(X.shape[0])
    np.random.shuffle(index)

    return X[index], y[index]