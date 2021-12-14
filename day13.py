import numpy as np


def read_data(filename: str) -> tuple:
    with open(filename) as f:
        parts = f.read().split("\n\n")
        dots = np.array([line.split(",") for line in parts[0].split("\n")],
                        dtype=int)
        directions = [l.split("=")[0][-1] for l in  parts[1].split("\n")]
        matrix = np.zeros(np.ndarray.astype(2*np.ceil(dots.max(axis=0)/2) + 1,
                                            int))
        matrix[tuple(dots.T)] = 1
        return matrix, directions


def fold(matrix: np.ndarray, direction: str) -> np.ndarray:
    if direction == "x":
        n = int(matrix.shape[0]/2)
        folding_matrix = np.hstack([np.eye(n), np.zeros([n, 1]),
                                    np.eye(n)[:, -1::-1]])
        return np.matmul(folding_matrix, matrix)

    elif direction == "y":
        n = int(matrix.shape[1]/2)
        folding_matrix = np.vstack([np.eye(n)[:, -1::-1],
                                    np.zeros([1, n]), np.eye(n)])
        return np.matmul(matrix, folding_matrix)


def task1(matrix: np.ndarray, directions: str) -> int:
    return (fold(matrix, directions[0]) > 0).sum()


def task2(matrix: np.ndarray, directions: str) -> np.ndarray:
    np.set_printoptions(linewidth=1000)
    for direction in directions:
        matrix = fold(matrix, direction)
    output = (np.array((np.rot90(matrix)>0), dtype=object)*'#'
              + np.array((np.rot90(matrix)<1), dtype=object)*'.')
    return output


if __name__ == "__main__":

    matrix, folds = read_data("input13.txt")

    print("task1:\t", task1(matrix, folds))

    print("task2:", end="")
    [print("\t", line) for line in task2(matrix, folds)]
