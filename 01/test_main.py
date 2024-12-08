from unittest import TestCase
from .main import part_one, part_two


class TestDayOne(TestCase):
    def test_part_one(self):
        received = part_one("01/data/example.txt")
        self.assertEqual(received, 11)

    def test_part_two(self):
        received = part_two("01/data/example.txt")
        self.assertEqual(received, 31)
