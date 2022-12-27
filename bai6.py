import numpy as np
import pandas as pd


def calculate_distance(x, y):
    dist = np.sqrt(np.sum([(a - b) * (a - b) for a, b in zip(x, y)]))
    return dist


def main():
    x = pd.Series([1, 5, 8, 9, 6, 7])
    y = pd.Series([2, 5, 4, 11, 13, 9, 6])
    print(calculate_distance(x, y))
