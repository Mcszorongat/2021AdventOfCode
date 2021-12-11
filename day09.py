import numpy as np
from skimage import measure


def read_data(filename: str) -> np.ndarray:
    with open(filename) as f:
        lines = f.read().split("\n")
    return np.array([[int(char) for char in line] for line in lines])


def hpossiblity(height_map: np.ndarray) -> np.ndarray:
    height, _ = height_map.shape
    diff_mx = height_map[:, 0:-1] - height_map[:, 1:]
    right_mask = np.hstack([np.zeros([height, 1]), diff_mx]) > 0
    left_mask = np.hstack([-diff_mx, np.zeros([height, 1])]) > 0
    return np.hstack([left_mask[:, 0:1],
                      left_mask[:, 1:-1] & right_mask[:, 1:-1],
                      right_mask[:, -1:]])


def task1(height_map: np.ndarray) -> int:
    mask_horizontal = hpossiblity(height_map=height_map)
    mask_vertical = np.rot90(hpossiblity(height_map=np.rot90(height_map)), k=3)
    min_mask = mask_horizontal & mask_vertical
    return height_map[min_mask].sum() + min_mask.sum()


def task2(height_map: np.ndarray) -> int:
    labels = measure.label((height_map != 9), connectivity=1)
    areas = np.unique(labels, return_counts=True)[1][1:]
    return np.prod(sorted(areas)[-3:])


if __name__ == "__main__":

    height_map = read_data("input09.txt")

    print("task1:\t", task1(height_map=height_map))

    print("task2:\t", task2(height_map=height_map))
