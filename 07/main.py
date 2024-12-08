from itertools import product
from typing import List
from helpers import read_file, execute


class SolutionFinder:
    def __init__(self, operators: List[str]):
        self.operators = operators

    def calc_row(self, row):
        combinations = self._get_combinations(row)
        target = self._get_target(row)
        for combo in combinations:
            equation = self._get_numbers(row)
            total = equation[0]
            for number in equation[1:]:
                operator = combo.pop()
                if operator == "||":
                    total = int(f"{total}{number}")
                elif operator == "+":
                    total += number
                elif operator == "*":
                    total = total * number
                else:
                    raise ValueError(f"The operator: {operator} is not supported")
            if total == target:
                return target
        return 0

    def _get_combinations(self, row) -> List[List[str]]:
        combo_length = row.split(": ")[1].count(" ")
        combinations = list(product(self.operators, repeat=combo_length))
        return [list(combo) for combo in combinations]

    def _get_target(self, row) -> int:
        return int(row.split(":")[0])

    def _get_numbers(self, row) -> List[int]:
        return [int(r) for r in row.split(": ")[1].split(" ")]


def part_one():
    solution_finder = SolutionFinder(["*", "+"])
    total = 0
    for row in read_file("07/7.in"):
        total += solution_finder.calc_row(row)
    print(f"Part One: {total}")


def part_two():
    solution_finder = SolutionFinder(["*", "+", "||"])
    total = 0
    for row in read_file("07/7.in"):
        total += solution_finder.calc_row(row)
    print(f"Part Two: {total}")


if __name__ == "__main__":
    execute(part_one, part_two)
