import numpy as np


def multiply_matrices(a, b):
    return a @ b


def main():
    a = np.array([[1, 3, 4], [-2, 6, 0], [-5, 7, 2]])
    b = np.array([[2, 3, 4], [-1, -2, -3], [0, 4, -4]])
    print(multiply_matrices(a, b))
    print(multiply_matrices(b, a))
