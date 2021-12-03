import pandas as pd


def decode_course(course: list) -> dict:
    split_course = [[line.split(' ')[0], int(line.split(' ')[1])]
                    for line in course]
    course_dicts = [{x[0]: x[1]} for x in split_course]
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
    with open("input2.txt") as f:
        course = f.read().splitlines()
    # course = ["forward 5", "down 5",
    #           "forward 8", "up 3", "down 8", "forward 2"]
    direction_df = decode_course(course)

    print("task1: ", task1(direction_df=direction_df))

    print("task2: ", task2(direction_df=direction_df))
