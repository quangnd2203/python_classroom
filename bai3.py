import pandas as pd


def get_element_not_common(a: pd.Series, b: pd.Series):
    series_c: pd.Series
    series_c = a+b
    for k, v in series_c.items():
        if v != 2:
            print(k)


def main():
    a = [1, 5, 8, 9, 6, 7]
    b = [2, 5, 4, 11, 13, 9, 6]

    series_a = pd.Series([1] * len(a), a)
    series_b = pd.Series([1] * len(b), b)
    get_element_not_common(series_a, series_b)
