import numpy as np



def decode(report):
    return np.array([",".join(x).split(",") for x in report], dtype=int)


def convert(x):
    return int("".join(np.array(x, dtype=str)), 2)


def task1(matrix):
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


def task2(matrix):
    oxygen_generator_rating = convert(search(type="oxygen", mat=matrix))
    co2_scrubber_rating = convert(search(type="co2", mat=matrix))
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    with open("input3.txt") as f:
        report = f.read().splitlines()
    # report = ["00100", "11110", "10110", "10111", "10101", "01111",
    #       "00111", "11100", "10000", "11001", "00010", "01010"]

    matrix = decode(report)

    print("task1: ", task1(matrix=matrix))

    print("task1: ", task2(matrix=matrix))
