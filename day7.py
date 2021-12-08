import numpy as np


def read_data(filename: str) -> np.ndarray:
    with open(filename) as f:
        initial_values = f.read()
    return np.array(initial_values.split(","), dtype=np.int64)


def task1(positions: np.ndarray) -> int:
    return int(np.abs(positions - np.median(positions)).sum())


def task21(positions: np.ndarray) -> int:
    """SLOW WITH WIDE RANGE"""
    return int(min(
        [(np.abs(positions - x) * (np.abs(positions - x) + 1) / 2).sum()
         for x in range(positions.min(), positions.max(), 1)]
    ))


def task22(positions: np.ndarray) -> int:
    mean = positions.mean()
    diff = sum(positions > mean) - sum(positions < mean)
    increment = 0.5 / positions.shape[0]

    optimal_x = mean + increment * diff
    if sum(positions == mean):
        correction = min([np.abs(diff), sum(positions == mean)])
        optimal_x += np.sign(mean - optimal_x) * increment * correction
    rx = np.round(optimal_x)    # rounded optimal x

    return int(sum(np.abs(positions - rx) * (np.abs(positions - rx) + 1) / 2))


if __name__ == "__main__":

    positions = read_data("input7.txt")

    print("task1:\t", task1(positions=positions))

    print("task2:\t", task22(positions=positions))
