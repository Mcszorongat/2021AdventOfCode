def read_data(filename: str) -> list:
    with open(filename) as f:
        return [x.split("-") for x in f.read().split("\n")]


def pairs2neigbor_dict(pairs: list) -> dict:
    tmp = pairs + [[x[1], x[0]] for x in pairs]
    neighbor_dict = {y: set() for y in [x[0] for x in tmp]}
    for pair in tmp:
        neighbor_dict[pair[0]].add(pair[1])
    return neighbor_dict


def walk_through(neighbor_dict: dict,
                 current_name: str="start", taboo_set: set=None):

    if taboo_set is None:
        taboo_set = set()

    if current_name.lower() == current_name:
        exception = set([current_name])
    else:
        exception = set([])

    if not (neighbor_dict[current_name] - taboo_set) or current_name == "end":
        return [[current_name]]

    tmp_list = []
    for next_point in neighbor_dict[current_name] - taboo_set:
        tmp_list.extend(walk_through(neighbor_dict, current_name=next_point,
                                     taboo_set=(taboo_set | exception)))

    return [[current_name] + lst for lst in tmp_list]



def task1(neighbor_dict: dict) -> int:
    paths = walk_through(neighbor_dict)
    valid_paths = [path for path in paths if path[-1] == "end"]
    return len(valid_paths)


def walk_through_repetition(neighbor_dict: dict,
                            current_name: str="start", taboo_set: set=None,
                            visited_small_caves: set=None) -> list:
    
    if taboo_set is None:
        taboo_set = set(["start"])
    if visited_small_caves is None:
        visited_small_caves = set()

    exception = set([])
    if current_name.lower() == current_name:
        if len(taboo_set) > 1:
            exception = set([current_name])
        elif current_name in visited_small_caves:
            exception = visited_small_caves
        else:
            visited_small_caves = visited_small_caves | set([current_name])

    if not (neighbor_dict[current_name] - taboo_set) or current_name == "end":
        return [[current_name]]

    tmp_list = []
    for next_point in neighbor_dict[current_name] - (taboo_set | exception):
        tmp_list.extend(
            walk_through_repetition(neighbor_dict, current_name=next_point,
                                    taboo_set=(taboo_set | exception),
                                    visited_small_caves=visited_small_caves)
        )

    return [[current_name] + lst for lst in tmp_list]


def task2(neighbor_dict: dict) -> int:
    paths = walk_through_repetition(neighbor_dict)
    valid_paths = [path for path in paths if path[-1] == "end"]
    return len(valid_paths)


if __name__ == "__main__":

    pairs = read_data("input12.txt")

    neighbor_dict = pairs2neigbor_dict(pairs)

    print("task1:\t", task1(neighbor_dict))

    print("task2:\t", task2(neighbor_dict))
