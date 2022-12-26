import random
import numpy as np


def create_matrix(m, n):
    matrix = []
    for i in range(m):
        new = []
        for j in range(n):
            new.append(round(random.random() * 100))
        matrix.append(new)
    return np.array(matrix)


def main():
    matrix = create_matrix(10, 10)
    print(matrix)
