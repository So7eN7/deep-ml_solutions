import math
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
    probabilities = []

    for i in features:
        z = 0
        for j, k in zip(weights, i):
            z += j * k
        z += bias
        prob = 1 / (1 + math.exp(-z))
        probabilities.append(round(prob, 4))

    mse = sum((i - j) ** 2 for i, j in zip(probabilities, labels)) / len(labels)
    mse = round(mse, 4)
    return probabilities, mse