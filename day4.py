import numpy as np


def read_data(filename: str) -> tuple:
    with open(filename, "r") as f:
        groups = f.read().split("\n\n")
    random_numbers = np.array(groups[0].split(","), dtype=int)
    matrices = np.array(
        [[row.split() for row in group.split("\n")] for group in groups[1:]],
        dtype=int
    )
    return random_numbers, matrices


def is_winner(matrix: np.ndarray) -> bool:
    dim = matrix.shape[0]
    if any(matrix.sum(axis=0) == -dim) or any(matrix.sum(axis=1) == -dim):
        return True
    else:
        return False


def find_winner(matrices: np.ndarray, random_numbers: np.ndarray) -> tuple:
    is_winner_list = [is_winner(matrix) for matrix in matrices]
    if any(is_winner_list):
        return is_winner_list.index(True), len(random_numbers)
    else:
        return find_winner(
            matrices=[np.where(matrix == random_numbers[0], -1, matrix)
                      for matrix in matrices],
            random_numbers=random_numbers[1:]
        )


def task1(random_numbers: np.ndarray, matrices: np.ndarray) -> tuple:
    idx, steps_left = find_winner(matrices=matrices,
                                  random_numbers=random_numbers)
    winner_numbers = matrices[idx].flatten()
    marked_numbers = np.intersect1d(winner_numbers,
                                    random_numbers[0:-steps_left])
    unmarked_sum = winner_numbers.sum() - marked_numbers.sum()
    return unmarked_sum * random_numbers[-steps_left-1], idx


def task2(random_numbers: np.ndarray, matrices: np.ndarray) -> tuple:
    indices_left = list(range(len(matrices)))
    while indices_left:
        score, idx = task1(random_numbers, matrices[indices_left])
        indices_left.pop(idx)
    return score, idx


if __name__=="__main__":
    random_numbers, matrices = read_data("input4.txt")

    print("task1:\t", 
          task1(random_numbers=random_numbers, matrices=matrices)[0])

    print(task2(random_numbers=random_numbers, matrices=matrices)[0])