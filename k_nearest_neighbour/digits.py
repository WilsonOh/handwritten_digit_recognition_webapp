from collections import Counter
import numpy as np


def initialise_training_samples(cls, file):
    with open(file) as f:
        n = int(f.readline()[:-1])
        obj_list = [cls() for _ in range(n)]
        for digit in obj_list:
            digit.read_digits(f)
    return obj_list


def initialise_testing_sample(cls, grid):
    test = cls()
    test.read_digits(grid)
    return test


def get_diff(digit1, digit2) -> np.ndarray:
    return np.sum(digit1 != digit2)


def find_most_common(training_samples, test_sample, K):
    for training_sample in training_samples:
        training_sample.distance = get_diff(test_sample.ar, training_sample.ar)
    return Counter(find_k_nearest(training_samples, K)).most_common(1)[0][0]


def find_k_nearest(training_samples, K):
    k_nearest = np.sort(training_samples)[:K]
    return [digit.label for digit in k_nearest]
