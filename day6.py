import numpy as np


def read_data(filename: str) -> np.ndarray:
    with open(filename) as f:
        initial_values = f.read()
    return np.array([initial_values.split(",")], dtype=int)


def task1(values: np.ndarray, days: int,
          cycle_days: int=7, newborn_delay: int=3) -> int:

    for _ in range(days):
        values = np.hstack([np.where(values == 0, cycle_days, values) - 1,
                           [np.full(np.where(values == 0)[1].shape[0],
                                    cycle_days + newborn_delay - 2)]])
    return values.shape[1]


def transform_data(values: np.ndarray, cycle_days: int,
                   newborn_delay: int) -> np.ndarray:

    return np.array(
        [[(values == i).sum() for i in range(cycle_days + newborn_delay - 1)]],
        dtype='int64'
    )


def elapse_day(values: np.ndarray, cycle_days: int) -> np.ndarray:
    return np.hstack(
        [
            values[:, 1:cycle_days],                                  # 0:5-1:6
            values[:, cycle_days:cycle_days + 1] + values[:, 0:1],    #  6 -7+0
            values[:, cycle_days + 1:],                               #  7 - 8:
            values[:, 0:1]                                            #  8 - 0
        ]
    )


def task2(values: np.ndarray, days: int,
          cycle_days: int=7, newborn_delay: int=3) -> int:

    transformed_values = transform_data(values=values, cycle_days=cycle_days,
                                        newborn_delay=newborn_delay)
    for _ in range(days):
        transformed_values = elapse_day(values=transformed_values,
                                        cycle_days=cycle_days)
    return transformed_values.sum()


if __name__ == "__main__":

    initial_values = read_data("input6.txt")

    print("task1:\t", task1(values=initial_values, days=80))

    print("task2:\t", task2(initial_values, days=256))
