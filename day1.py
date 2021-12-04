import numpy as np


def read_data(filename: str) -> np.ndarray:
    with open(filename) as f:
        return np.fromfile(f, dtype=int, count=-1, sep="\n")


def task1(depths: np.ndarray) -> int:
    return sum(np.diff(depths)>0)


def rolling_sum(array: np.ndarray, window_width: int=3) -> np.ndarray:
    temp = np.cumsum(array, dtype=int)
    temp[window_width:] = temp[window_width:] - temp[:-window_width]
    return temp[window_width - 1:]


def task2(depths: np.ndarray, window_width: int=3) -> int:
    depths_cum = rolling_sum(array=depths, window_width=window_width)
    return sum(np.diff(depths_cum)>0)


if __name__ == "__main__":

    depths = read_data("input1.txt")
    # depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    print("task1:\t", task1(depths))

    print("task2:\t", task2(depths))
