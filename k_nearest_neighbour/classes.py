import numpy as np


class Digit:
    def __init__(self):
        self.ar = None
        self.label = None

    def read_digits(self, f) -> None:
        self.label = f.readline()
        self.ar = np.array([list(f.readline())[:-1] for _ in range(28)])


class Test(Digit):
    def __init__(self):
        super().__init__()

    def read_digits(self, grid) -> None:
        self.ar = np.array([['#' if elem else '.' for elem in row] for row in grid])


class Neighbour(Digit):
    def __init__(self):
        super().__init__()
        self.distance = 0

    def __gt__(self, other):
        return self.distance > other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __repr__(self):
        return f"Label: {self.label}, Distance: {self.distance}"
