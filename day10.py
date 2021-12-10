pair_dict = {"(": ")", "[": "]", "{": "}", "<": ">"}
opening_characters = ["(", "[", "{", "<"]


def read_data(filename: str) -> list:
    with open(filename) as f:
        return f.read().split("\n")


def find_characters(lines: list) -> tuple:
    invalid_characters = []
    correct_endings = []

    for line in lines:
        expected_character_list = []
        for character in line:
            if character in opening_characters:
                expected_character_list.append(pair_dict[character])
            elif character == expected_character_list[-1]:
                expected_character_list = expected_character_list[0:-1]
            else:
                invalid_characters.append(character)
                expected_character_list = []
                break

        if expected_character_list:
            correct_endings.append(expected_character_list[-1::-1])

    return invalid_characters, correct_endings


def task1(lines: list) -> int:
    character_value_dict = {"(": 3, "[": 57, "{": 1197, "<": 25137,
                            ")": 3, "]": 57, "}": 1197, ">": 25137}

    invalid_characters, _ = find_characters(lines=lines)

    return sum([character_value_dict[char] for char in invalid_characters])


def task2(lines: list) -> int:
    character_value_dict = {")": 1, "]": 2, "}": 3, ">": 4}

    _, correct_endings = find_characters(lines)
    line_sums = [sum([character_value_dict[char]*(5**(len(line)-i-1))
                      for i, char in enumerate(line)])
                 for line in correct_endings]
    # If it really is always odd.
    return sorted(line_sums)[int(len(line_sums)/2)]


if __name__ == "__main__":

    lines = read_data("input10.txt")

    print("task1:\t", task1(lines=lines))

    print("task2:\t", task2(lines=lines))
