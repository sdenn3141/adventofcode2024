from unittest import TestCase
from helpers import read_file
from .main import AntiNodeLocator, part_one, part_two


class TestDay8PartOne(TestCase):
    def test_locate_nodes(self):
        f = read_file("08/data/example1.txt")
        area = [list(s) for s in f]
        locator = AntiNodeLocator(area, False)
        locator.locate_nodes()
        received = locator.nodes
        expected = {
            "0": [[1, 8], [2, 5], [3, 7], [4, 4]],
            "A": [[5, 6], [8, 8], [9, 9]],
        }
        self.assertEqual(received, expected)

    def test_mark_antinodes(self):
        f = read_file("08/data/example1.txt")
        area = [list(s) for s in f]
        locator = AntiNodeLocator(area, False)
        locator.locate_nodes()
        locator.mark_antinodes()
        received = locator.area
        expected = [list(s) for s in read_file("08/data/example3.txt")]
        self.assertEqual(expected, received)

    def test_example_one(self):
        received = part_one("08/data/example1.txt")
        expected = 14
        self.assertEqual(received, expected)


class TestDay8PartTwo(TestCase):
    def test_example_one(self):
        received = part_two("08/data/example1.txt")
        expected = 34
        self.assertEqual(received, expected)

    def test_example_two(self):
        received = part_two("08/data/example2.txt")
        expected = 9
        self.assertEqual(received, expected)
