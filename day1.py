import os
import numpy as np


if __name__ == "__main__":
    with open("input1.txt") as f:
        depths = np.fromfile(f, dtype=int, count=-1, sep="\n")
    # depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    print("task1:\t", sum(np.diff(depths)>0))

    new_length = len(depths)-2
    depths_cum = sum(np.array([depths[i:new_length+i] for i in range(3)]))
    print("task2:\t", sum(np.diff(depths_cum)>0))
