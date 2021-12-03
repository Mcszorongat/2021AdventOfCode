import numpy as np


if __name__ == "__main__":
    with open("input1.txt") as f:
        depths = np.fromfile(f, dtype=int, count=-1, sep="\n")
    # depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    print("task1:\t", sum(np.diff(depths)>0))

    window_width = 3
    new_length = len(depths) - window_width + 1
    depths_cum = sum(
        np.array([depths[i:new_length+i] for i in range(window_width)])
    )
    print("task2:\t", sum(np.diff(depths_cum)>0))
