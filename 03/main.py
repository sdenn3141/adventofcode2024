from helpers import read_file, execute
from re import findall, fullmatch, split


def part_one(file_name="03/data/3.in"):
    f = "".join(read_file(file_name))
    pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    matches = findall(pattern, f)
    total = sum(int(x) * int(y) for x, y in matches)
    print(f"Part One: {total}")
    return total


def part_two(file_name="03/data/3.in"):
    f = "".join(read_file(file_name))
    mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    do_pattern = r"do\(\s*\)"
    dont_pattern = r"don't\(\s*\)"
    tokens = split(r"(mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\)|do\(\s*\)|don't\(\s*\))", f)

    is_enabled = True
    total = 0

    for token in tokens:
        token = token.strip()
        if not token:
            continue
        if fullmatch(do_pattern, token):
            is_enabled = True
        elif fullmatch(dont_pattern, token):
            is_enabled = False
        elif fullmatch(mul_pattern, token):
            if is_enabled:
                x, y = map(int, findall(r"\d+", token))
                total += x * y
    print(f"Part Two: {total}")
    return total


if __name__ == "__main__":
    execute(part_one, part_two)
