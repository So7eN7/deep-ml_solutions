import numpy as np

def make_diagonal(x):
	# Your code here
    identity_mat = np.identity(np.size(x))
    res = identity_mat * x
    return res