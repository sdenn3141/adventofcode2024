from unittest import TestCase
from .main import part_one, part_two


class TestPartSix(TestCase):
    def test_part_one(self):
        received = part_one("03/data/example1.txt")
        self.assertEqual(received, 161)

    def test_part_two(self):
        received = part_two("03/data/example2.txt")
        self.assertEqual(received, 48)
