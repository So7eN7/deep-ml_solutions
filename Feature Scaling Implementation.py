import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	max_ = np.max(data, axis=0)
	min_ = np.min(data, axis=0)
	standardized_data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
	normalized_data = (data - min_) / (max_ - min_) 
	return np.round(standardized_data, 4).tolist(), np.round(normalized_data, 4).tolist()