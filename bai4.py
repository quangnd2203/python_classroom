import pandas as pd


def take_multiples(series: pd.Series, number: int):
    for k, v in series.items():
        if v % number == 0:
            print(k)


def main():
    a = [1, 5, 8, 9, 6, 7]
    series_a = pd.Series(a)
    take_multiples(series_a, 3)
