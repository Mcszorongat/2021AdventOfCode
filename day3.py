import numpy as np


def read_data(filename: str) -> np.ndarray:
    with open(filename) as f:
        report = f.read().splitlines()
    return np.array([",".join(x).split(",") for x in report], dtype=int)


def convert(x: np.ndarray) -> int:
    return (x * 2 ** np.arange(len(x) - 1, -1, -1, dtype='int64')).sum()


def task1(matrix: np.ndarray) -> int:
    most_common = matrix.mean(axis=0)>0.5
    gamma = convert(most_common.astype(int))
    epsilon = convert((~most_common).astype(int))
    return gamma * epsilon


def search(type: str, mat: np.ndarray, digit: int=0) -> np.ndarray:
    if mat.shape[0] == 1:
        return mat[0]
    else:
        if type == "oxygen":
            return search(
                type=type,
                mat=mat[mat[:, digit] ==
                        (mat[:, digit].mean(axis=0)>=0.5).astype(int)],
                digit=digit + 1
            )
        if type == "co2":
            return search(
                type=type,
                mat=mat[mat[:, digit] ==
                        (mat[:, digit].mean(axis=0)<0.5).astype(int)],
                digit=digit + 1
            )


def task2(matrix: np.ndarray) -> int:
    oxygen_generator_rating = convert(search(type="oxygen", mat=matrix))
    co2_scrubber_rating = convert(search(type="co2", mat=matrix))
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":

    matrix = read_data("input3.txt")

    print("task1: ", task1(matrix=matrix))

    print("task1: ", task2(matrix=matrix))
