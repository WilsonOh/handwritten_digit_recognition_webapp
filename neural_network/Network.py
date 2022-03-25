import numpy as np
import random


class Network:
    def __init__(self, sizes, weights=None, biases=None):
        self.layers = len(sizes)
        self.sizes = sizes
        self.weights = weights if weights is not None else np.array([np.random.randn(row, col) for row, col in zip(sizes[1:], sizes[:-1])], dtype=object)
        self.biases = biases if biases is not None else np.array([np.random.randn(row, 1) for row in sizes[1:]], dtype=object)

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid((w @ a) + b)
        return a

    def test(self, test_data):
        print(f"Accuracy: {self.evaluate(test_data)} / {len(test_data)}")

    def show_num(self, a):
        return np.argmax(self.feedforward(a))

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        n_train = len(training_data)
        
        for i in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[i: i + mini_batch_size] for i in range(0, n_train, mini_batch_size)]
            
            for mini_batch in mini_batches:
                self.train(mini_batch, eta)
            if test_data:
                print(f"Epoch {i}: {self.evaluate(test_data)} / {len(test_data)}")
            else:
                print(f"Epoch {i} complete")

    def train(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_w, delta_b = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_w)]
        self.weights = np.array([w - (eta/len(mini_batch) * nw) for w, nw in zip(self.weights, nabla_w)], dtype=object)
        self.biases = np.array([b - (eta/len(mini_batch) * nb) for b, nb in zip(self.biases, nabla_b)], dtype=object)

    def backprop(self, digit, label):
        total_weight_delta = [np.zeros(b.shape) for b in self.biases]
        total_bias_delta = [np.zeros(w.shape) for w in self.weights]
        activation = digit
        activations = [digit]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = (w @ activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        dC_dB = sigmoid_prime(zs[-1]) * (activations[-1] - label)
        dC_dW = dC_dB @ activations[-2].T
        total_weight_delta[-1] = dC_dW
        total_bias_delta[-1] = dC_dB
        for i in range(2, self.layers):
            dC_dB = (self.weights[-i + 1].T @ dC_dB) * sigmoid_prime(zs[-i])
            dC_dW = dC_dB @ activations[-i - 1].T
            total_weight_delta[-i] = dC_dW
            total_bias_delta[-i] = dC_dB
        return total_weight_delta, total_bias_delta

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y) for x, y in test_data]
        return sum(x == y for x, y in test_results)

    def save_params(self):
        np.save('weights.npy', self.weights, allow_pickle=True)
        np.save('biases.npy', self.biases, allow_pickle=True)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z) * (1 - sigmoid(z))
