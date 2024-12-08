from unittest import TestCase
from .main import part_one, part_two


class TestPartTwo(TestCase):
    def test_part_one(self):
        received = part_one("02/data/example.txt")

        self.assertEqual(received, 2)

    def test_part_two(self):
        received = part_two("02/data/example.txt")
        self.assertEqual(received, 4)
