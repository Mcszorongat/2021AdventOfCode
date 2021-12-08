def read_data(filename: str) -> list:
    with open(filename) as f:
        lines = f.read().split("\n")
    return ([[x for x in line.split(" | ")[0].split(" ")] for line in lines],
            [[x for x in line.split(" | ")[1].split(" ")] for line in lines])


def task1(output_list: list) -> int:
    lengths = [y for x in [list(map(lambda x: len(x), line))
                           for line in output_list] for y in x]
    return (sum(map(lambda x: 1 if x < 5 else 0, lengths))
            + sum(map(lambda x: 1 if x > 6 else 0, lengths)))


def decode_patterns(patterns_list):
    patterns = set(patterns_list)
    inverse_dict = {i: None for i in range(10)}

    condition = [
        None,
        lambda _, p: len(p) == 2,                                       # 1
        lambda d, p: (len(p) == 5) & (set(p + d[4]) == set(d[8])),      # 2
        lambda d, p: (len(p) == 5) & (set(p + d[1]) == set(p)),         # 3
        lambda _, p: len(p) == 4,                                       # 4
        lambda d, p: (len(p) == 5) & (set(p + d[2]) == set(d[8])),      # 5
        lambda d, p: (len(p) == 6) & (set(p + d[1]) == set(d[8])),      # 6
        lambda _, p: len(p) == 3,                                       # 7
        lambda _, p: len(p) == 7,                                       # 8
        lambda d, p: (len(p) == 6) & (set(p + d[3]) == set(p))          # 9
    ]

    for pattern in patterns:
        if condition[1](inverse_dict, pattern): inverse_dict[1] = pattern
        elif condition[4](inverse_dict, pattern): inverse_dict[4] = pattern
        elif condition[7](inverse_dict, pattern): inverse_dict[7] = pattern
        elif condition[8](inverse_dict, pattern): inverse_dict[8] = pattern

    for pattern in patterns - set(inverse_dict.values()):
        if condition[2](inverse_dict, pattern): inverse_dict[2] = pattern
        elif condition[3](inverse_dict, pattern): inverse_dict[3] = pattern
        elif condition[6](inverse_dict, pattern): inverse_dict[6] = pattern

    for pattern in patterns - set(inverse_dict.values()):
        if condition[5](inverse_dict, pattern): inverse_dict[5] = pattern
        elif condition[9](inverse_dict, pattern): inverse_dict[9] = pattern

    inverse_dict[0] = (patterns - set(inverse_dict.values())).pop()

    return {''.join(sorted(key)): value for value, key in inverse_dict.items()}


def convert_numbers(dec_dct: dict, str_list: list) -> int:
    number_list = [10**(len(str_list)-i-1) * dec_dct[''.join(sorted(string))]
                   for i, string in enumerate(str_list)]
    return sum(number_list)


def task2(data: list) -> int:
    numbers = [convert_numbers(decode_patterns(pattern), number_string_list)
               for pattern, number_string_list in zip(data[0], data[1])]
    return sum(numbers)


if __name__ == "__main__":

    data = read_data("input8.txt")

    print("task1:\t", task1(output_list=data[1]))

    print("task2:\t", task2(data=data))
