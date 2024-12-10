from unittest import TestCase
from .main import part_one, part_two


class TestDay8PartOne(TestCase):
    def test_example_one(self):
        received = part_one("10/data/example1.txt")
        expected = 36
        self.assertEqual(received, expected)


class TestDay8PartTwo(TestCase):
    def test_example_one(self):
        received = part_two("10/data/example1.txt")
        expected = 0
        self.assertEqual(received, expected)