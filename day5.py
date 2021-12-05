import numpy as np


def read_data(filename: str) -> np.ndarray:
    with open(filename) as f:
        lines = f.read().splitlines()
    return np.array(
        [[[int(value) for value in coordinate.split(",")]
          for coordinate in line.split(" -> ")]
         for line in lines]
    )


def task1(line_coordinates: np.ndarray) -> int:
    horz_vert_line_coordinates = line_coordinates[
        [not all(line)
         for line in (line_coordinates[:, 0] - line_coordinates[:, 1])]
    ]

    cloud_map = np.zeros([horz_vert_line_coordinates.max(),
                          horz_vert_line_coordinates.max()])
    
    all_points = np.array([], dtype=int)
    for line in horz_vert_line_coordinates:
        const_mask = ((line[0] - line[1])==0) * np.array([1, 1])
        varying_mask = np.matmul(const_mask, np.array([[0,1], [1,0]]))
        offset = line[0] * const_mask

        start = min(sum(line[0] - offset), sum(line[1] - offset))
        end = max(sum(line[0] - offset), sum(line[1] - offset))
        points = np.array(range(start, end + 1, 1))
        raw_points = np.matmul(np.transpose([points]),
                               np.atleast_2d(varying_mask))
        abs_points = raw_points + offset
        if len(all_points) != 0:
            all_points = np.append(all_points, abs_points, axis=0)
        else:
            all_points = abs_points
    _, counts = np.unique(all_points, axis=0, return_counts=True)
    return sum(counts > 1)



if __name__ == "__main__":
    line_coordinates = read_data("input5.txt")

    print("task1:\t", task1(line_coordinates=line_coordinates))