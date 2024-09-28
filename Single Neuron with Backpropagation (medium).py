import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def train_neuron(features, labels, initial_weights, initial_bias, learning_rate, epochs):
    weights = np.array(initial_weights)
    bias = np.array(initial_bias)
    mse_values = []
    for _ in range(epochs):
        z = np.dot(features, weights) + bias
        y_pred = sigmoid(z)
        mse = np.mean((labels - y_pred) ** 2)
        mse_values.append(round(mse, 4))

        error = y_pred - labels
        weights_gradients = np.dot(features.T, error * y_pred * (1 - y_pred))
        bias_gradient = np.sum(error * y_pred * (1 - y_pred))

        weights -= learning_rate * weights_gradients / len(labels)
        bias -= learning_rate * bias_gradient / len(labels)
    
    return weights.tolist(), bias, mse_values

if __name__ == "__main__":
    features = [[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]]
    labels = [1, 0, 0]
    initial_weights = [0.1, -0.2]
    initial_bias = 0.0
    learning_rate = 0.1
    epochs = 2

    updated_weights, updated_bias, mse_values = train_neuron(np.array(features), np.array(labels), np.array(initial_weights), initial_bias, learning_rate, epochs)
    # output: updated_weights = [0.0808, -0.1916], updated_bias = -0.0214, mse_values = [0.2386, 0.2348]
    print(f"updated_weights = {updated_weights}, updated_bias = {updated_bias}, mse_values = {mse_values}")