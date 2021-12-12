import numpy as np
from numpy import linalg


def read_data(filename: str) -> np.ndarray:
    with open(filename) as f:
        lines = f.read().split("\n")
    return np.array([[int(char) for char in line] for line in lines])


def rot(a: float=np.pi/4) -> np.ndarray:
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])


def shift(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return np.pad(
        matrix,
        ((1 if vector[1]<-0.01 else 0, 1 if vector[1]>0.01 else 0),
         (1 if vector[0]>0.01 else 0, 1 if vector[0]<-0.01 else 0))
    )[1 if vector[1]>0.01 else 0: -1 if vector[1]<-0.01 else None,
      1 if vector[0]<-0.01 else 0: -1 if vector[0]>0.01 else None]


def expand_pattern(matrix: np.ndarray, neighbours_count=8) -> np.ndarray:
    vectors = [np.matmul(np.array([[0, 1]]), linalg.matrix_power(rot(), i))
               for i in range(neighbours_count)]
    return np.array([shift(matrix, vec[0]) for vec in vectors]).sum(axis=0)


def step(input_matrix: np.ndarray) -> tuple:
    input_matrix = input_matrix + 1
    availablity_map = np.ones_like(input_matrix)
    while (input_matrix*availablity_map>=10).sum():
        increment = expand_pattern(input_matrix*availablity_map>=10)
        availablity_map = availablity_map * (input_matrix<10)
        input_matrix = input_matrix + increment
    return input_matrix * availablity_map, availablity_map


def task1(input_matrix: np.ndarray, step_count: int) -> int:
    flash_counter = 0
    for _ in range(step_count):
        input_matrix, availability_map = step(input_matrix)
        flash_counter += (availability_map == 0).sum()
    return flash_counter


def task2(input_matrix: np.ndarray, max_step_count: int) -> int:
    for i in range(max_step_count):
        input_matrix, availability_map = step(input_matrix)
        if availability_map.sum() == 0:
            return i+1


if __name__ == "__main__":

    matrix = read_data("input11.txt")

    print("task1:\t", task1(input_matrix=matrix, step_count=100))

    print("task2:\t", task2(input_matrix=matrix,  max_step_count=1000))
