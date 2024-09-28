import math

def sigmoid(z: float) -> float:
    result = 1/(1+math.exp(-z))
    return result

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []
    for feature in features:
        z = sum([a*b for a, b in zip(feature, weights)]) + bias
        probabilities.append(sigmoid(z))
    
    mse = sum([(a-b)**2 for a, b in zip(probabilities, labels)])/len(labels)
    
    return probabilities, mse

if __name__=="__main__":
    features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
    labels = [0, 1, 0]
    weights = [0.7, -0.4]
    bias = -0.1
    print(single_neuron_model(features, labels, weights, bias)) # ([0.4626, 0.4134, 0.6682], 0.3349)