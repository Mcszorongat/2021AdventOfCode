import numpy as np
from collections import defaultdict


def read_data(filename: str) -> tuple:
    with open(filename) as f:
        parts = f.read().split("\n\n")
    pair_rule_dict = {x[0]: [x[0][0] + x[1], x[1] + x[0][1]] for x
                      in [l.split(" -> ") for l in  parts[1].split("\n")]}
    char_rule_dict = defaultdict(dict, {x[0]: x[1] for x in [l.split(" -> ")
                      for l in  parts[1].split("\n")]})
    return parts[0], pair_rule_dict, char_rule_dict


def task(template: str, pair_rule_dict: dict,
         char_rule_dict: dict, steps: int) -> list:
    characters = np.array(sorted(list(set(
        "".join([key + "".join(val) for key, val in pair_rule_dict.items()])
    ))))
    possible_pairs = np.array([x + y for x in characters for y in characters])

    actual_pairs = np.array([template.count(pair) for pair in possible_pairs],
                            dtype=np.int64)
    character_counts = np.array([template.count(c) for c in characters],
                                dtype=np.int64)
    step_matrix = np.array(
        [((possible_pairs == pair_rule_dict[pair][0])
          | (possible_pairs == pair_rule_dict[pair][1]))
         for pair in possible_pairs],
        dtype=int)

    increment_matrix = np.array([characters == char_rule_dict[pair]
                                 for pair in possible_pairs], dtype=int)

    for _ in range(steps):
        character_counts += np.matmul(actual_pairs, increment_matrix)
        actual_pairs = np.matmul(actual_pairs, step_matrix)

    return sorted(character_counts)[-1] - sorted(character_counts)[0]


if __name__ == "__main__":

    template, pair_rule_dict, char_rule_dict = read_data("input14.txt")

    print("task1:\t", task(template, pair_rule_dict, char_rule_dict, 10))

    print("task1:\t", task(template, pair_rule_dict, char_rule_dict, 40))
