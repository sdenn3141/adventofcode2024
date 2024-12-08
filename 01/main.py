from helpers import read_file, execute


def part_one(file_name="01/data/1.in"):
    f = read_file(file_name)
    left_list = []
    right_list = []
    for line in f:
        split_line = line.split("   ")
        left_list.append(split_line[0])
        right_list.append(split_line[1])

    left_list.sort()
    right_list.sort()
    total = 0
    for i in range(len(left_list)):
        total += abs(int(left_list[i]) - int(right_list[i]))
    print(f"Part One: {total}")
    return total


def part_two(file_name="01/data/1.in"):
    f = read_file(file_name)
    left_list = []
    right_list = []
    for line in f:
        split_line = line.split("   ")
        left_list.append(split_line[0])
        right_list.append(split_line[1])

    total = 0
    for number in left_list:
        total += int(number) * right_list.count(number)
    print(f"Part Two: {total}")
    return total


if __name__ == "__main__":
    execute(part_one, part_two)
