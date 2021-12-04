import pandas as pd


def read_data(filename: str) -> pd.DataFrame:
    with open(filename) as f:
        lines = f.read().splitlines()
    course_dicts = [{line.split(' ')[0]: int(line.split(' ')[1])}
                    for line in lines]
    direction_df = pd.DataFrame(course_dicts)
    return direction_df.fillna(0)


def task1(direction_df: pd.DataFrame) -> int:
    forward_position = direction_df.sum()['forward']
    depth = direction_df.sum()['down'] - direction_df.sum()['up']
    return int(forward_position * depth)


def task2(direction_df: pd.DataFrame) -> int:
    task2_df = pd.DataFrame(
        data={"forward": direction_df["forward"],
              "aim": (direction_df.down - direction_df.up).cumsum()}
    )
    task2_df["x"] = task2_df["forward"].cumsum()
    task2_df["y"] = (task2_df["aim"] * task2_df["forward"]).cumsum()
    return int(task2_df.iloc[-1]["x"] * task2_df.iloc[-1]["y"])


if __name__ == "__main__":
    
    direction_df = read_data("input2.txt")

    print("task1:\t", task1(direction_df=direction_df))

    print("task2:\t", task2(direction_df=direction_df))
