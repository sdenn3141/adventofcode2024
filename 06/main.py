from helpers import read_file, execute


class Guard:
    def __init__(self, area):
        self.direction = "N"
        self.area = area
        self.previous_rotations = []
        start_x, start_y = [
            (j, i)
            for i, row in enumerate(area)
            for j, elem in enumerate(row)
            if elem == "^"
        ][0]
        self.x = start_x
        self.y = start_y
        self.finish = False

    def walk_forward(self):
        self.area[self.y][self.x] = "X"
        match self.direction:
            case "N":
                self._walk_north()
            case "E":
                self._walk_east()
            case "S":
                self._walk_south()
            case "W":
                self._walk_west()
            case _:
                "Invalid direction"

    def _walk_north(self):
        self.y += -1
        if self.area[self.y][self.x] == "#":
            self._walk_south()
            self._rotate()

    def _walk_south(self):
        self.y += 1
        if self.area[self.y][self.x] == "#":
            self._walk_north()
            self._rotate()

    def _walk_east(self):
        self.x += 1
        if self.area[self.y][self.x] == "#":
            self._walk_west()
            self._rotate()

    def _walk_west(self):
        self.x += -1
        if self.area[self.y][self.x] == "#":
            self._walk_east()
            self._rotate()

    def _rotate(self):
        match self.direction:
            case "N":
                self.direction = "E"
            case "E":
                self.direction = "S"
            case "S":
                self.direction = "W"
            case "W":
                self.direction = "N"
            case _:
                "Invalid direction"
        self.previous_rotations.append((self.x, self.y, self.direction))
        if self.previous_rotations.count((self.x, self.y, self.direction)) == 4:
            self.finish = True


def part_one(file_name="06/data/6.in"):
    f = read_file(file_name)
    area = [list(s) for s in f]
    guard = Guard(area)
    while True:
        try:
            guard.walk_forward()
            if guard.y < 0 or guard.x < 0:
                break
        except IndexError:
            break
    total = 0
    for row in guard.area:
        total += row.count("X")
    print(f"Part One: {total}")
    return total


def part_two(file_name="06/data/6.in"):
    f = read_file(file_name)
    area = [list(s) for s in f]
    total = 0

    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] == "#" or area[i][j] == "^":
                pass
            else:
                new_layout = [row[:] for row in area]
                new_layout[i][j] = "#"
                print(f"Row {i}: {new_layout[i]}")
                guard = Guard(new_layout)
                while True:
                    try:
                        if guard.finish == True:
                            total += 1
                            break
                        guard.walk_forward()
                        if guard.y < 0 or guard.x < 0:
                            break
                    except IndexError:
                        break
    print(f"Part Two: {total}")
    return total


if __name__ == "__main__":
    execute(part_one, part_two)
