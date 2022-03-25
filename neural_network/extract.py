import numpy as np


def load_MNIST_training_dataset(file):
    training_data = []
    with open(file) as f:
        n_train = int(next(f))
        for _ in range(n_train):
            label = create_label_vector(int(f.readline().strip()))
            digit = [list(f.readline().strip()) for _ in range(28)]
            digit = digit_processing(digit)
            training_data.append((digit, label))
    return training_data


def load_MNIST_testing_dataset(file):
    testing_data = []
    with open(file) as f:
        n_train = int(next(f))
        for _ in range(n_train):
            label = int(f.readline().strip())
            digit = [list(f.readline().strip()) for _ in range(28)]
            digit = digit_processing(digit)
            testing_data.append((digit, label))
    return testing_data


def load_from_grid(grid):
    grid = np.array(grid, dtype=int)
    return grid.reshape(784, 1)


def create_label_vector(label):
    tmp = np.zeros((10, 1))
    tmp[label] = 1
    return tmp


def digit_processing(digit):
    return np.array([[1 if c == '#' else 0 for c in row] for row in digit]).reshape(784, 1)
