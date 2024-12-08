from helpers import read_file, execute


def part_one(file_name="04/data/4.in"):
    def look_for_xmas(c, i, j, direction):
        try:
            match direction:
                case "N":
                    return (
                        True
                        if (
                            c[i][j - 1] == "M"
                            and c[i][j - 2] == "A"
                            and c[i][j - 3] == "S"
                        )
                        and j - 3 >= 0
                        else False
                    )
                case "NE":
                    return (
                        True
                        if (
                            c[i + 1][j - 1] == "M"
                            and c[i + 2][j - 2] == "A"
                            and c[i + 3][j - 3] == "S"
                        )
                        and j - 3 >= 0
                        else False
                    )
                case "E":
                    return (
                        True
                        if c[i + 1][j] == "M"
                        and c[i + 2][j] == "A"
                        and c[i + 3][j] == "S"
                        else False
                    )
                case "SE":
                    return (
                        True
                        if c[i + 1][j + 1] == "M"
                        and c[i + 2][j + 2] == "A"
                        and c[i + 3][j + 3] == "S"
                        else False
                    )
                case "S":
                    return (
                        True
                        if c[i][j + 1] == "M"
                        and c[i][j + 2] == "A"
                        and c[i][j + 3] == "S"
                        else False
                    )
                case "SW":
                    return (
                        True
                        if (
                            c[i - 1][j + 1] == "M"
                            and c[i - 2][j + 2] == "A"
                            and c[i - 3][j + 3] == "S"
                        )
                        and i - 3 >= 0
                        else False
                    )
                case "W":
                    return (
                        True
                        if (
                            c[i - 1][j] == "M"
                            and c[i - 2][j] == "A"
                            and c[i - 3][j] == "S"
                        )
                        and i - 3 >= 0
                        else False
                    )
                case "NW":
                    return (
                        True
                        if (
                            c[i - 1][j - 1] == "M"
                            and c[i - 2][j - 2] == "A"
                            and c[i - 3][j - 3] == "S"
                        )
                        and i - 3 >= 0
                        and j - 3 >= 0
                        else False
                    )
        except IndexError:
            return False

    total = 0
    f = read_file(file_name)
    c = [list(line) for line in f]
    for i in range(len(c)):
        for j in range(len(c)):
            if c[i][j] == "X":
                if look_for_xmas(c, i, j, "N"):
                    total += 1
                if look_for_xmas(c, i, j, "NE"):
                    total += 1
                if look_for_xmas(c, i, j, "E"):
                    total += 1
                if look_for_xmas(c, i, j, "SE"):
                    total += 1
                if look_for_xmas(c, i, j, "S"):
                    total += 1
                if look_for_xmas(c, i, j, "SW"):
                    total += 1
                if look_for_xmas(c, i, j, "W"):
                    total += 1
                if look_for_xmas(c, i, j, "NW"):
                    total += 1

    print(f"Part One: {total}")
    return total


def part_two(file_name="04/data/4.in"):
    total = 0
    f = read_file(file_name)
    c = [list(line) for line in f]
    for i in range(1, len(c) - 1):
        for j in range(1, len(c[i]) - 1):
            if c[i][j] == "A":
                if (
                    c[i - 1][j - 1] == "M"
                    and c[i + 1][j - 1] == "M"
                    and c[i - 1][j + 1] == "S"
                    and c[i + 1][j + 1] == "S"
                ):
                    total += 1
                elif (
                    c[i - 1][j - 1] == "M"
                    and c[i - 1][j + 1] == "M"
                    and c[i + 1][j - 1] == "S"
                    and c[i + 1][j + 1] == "S"
                ):
                    total += 1
                elif (
                    c[i + 1][j + 1] == "M"
                    and c[i - 1][j + 1] == "M"
                    and c[i + 1][j - 1] == "S"
                    and c[i - 1][j - 1] == "S"
                ):
                    total += 1
                elif (
                    c[i + 1][j + 1] == "M"
                    and c[i + 1][j - 1] == "M"
                    and c[i - 1][j + 1] == "S"
                    and c[i - 1][j - 1] == "S"
                ):
                    total += 1

    print(f"Part Two: {total}")
    return total


if __name__ == "__main__":
    execute(part_one, part_two)
