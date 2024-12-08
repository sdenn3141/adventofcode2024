from unittest import TestCase
from .main import part_one, part_two


class TestPartSix(TestCase):
    def test_part_one(self):
        received = part_one("04/data/example1.txt")
        self.assertEqual(received, 18)

    def test_part_two(self):
        received = part_two("04/data/example2.txt")
        self.assertEqual(received, 9)
