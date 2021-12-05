import numpy as np
from numpy import matlib as ml


def read_data(filename: str) -> np.ndarray:
    with open(filename) as f:
        lines = f.read().splitlines()
    return np.array(
        [[[int(value) for value in coordinate.split(",")]
          for coordinate in line.split(" -> ")]
         for line in lines]
    )


def line_to_points(line: np.ndarray) -> np.ndarray:
    p1 = line[0]
    v = line[1] - line[0]
    # v / np.abs(v).max() - only because of 45°
    v_steps = ml.repmat(v / np.abs(v).max(), np.abs(v).max(), 1).cumsum(axis=0)
    return np.append([p1], p1 + v_steps, axis=0)


def task1(line_coordinates: np.ndarray) -> int:
    horz_vert_line_coordinates = line_coordinates[
        [any(line == 0)
         for line in (line_coordinates[:, 0] - line_coordinates[:, 1])]
    ]
    points = np.vstack(
        [line_to_points(line) for line in horz_vert_line_coordinates]
    )
    _, counts = np.unique(points, axis=0, return_counts=True)
    return sum(counts > 1)


def task2(line_coordinates: np.ndarray) -> int:
    points = np.vstack([line_to_points(line) for line in line_coordinates])
    _, counts = np.unique(points, axis=0, return_counts=True)
    return sum(counts > 1)



if __name__ == "__main__":
    line_coordinates = read_data("input5.txt")

    print("task1:\t", task1(line_coordinates=line_coordinates))

    print("task2:\t", task2(line_coordinates=line_coordinates))
