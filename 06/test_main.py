from unittest import TestCase
from .main import Guard, part_one, part_two
from helpers import read_file


class TestPartSix(TestCase):
    def test_moves_forward(self):
        layout = read_file("06/data/example.txt")
        area = [list(s) for s in layout]
        guard = Guard(area)
        guard.walk_forward()
        self.assertEqual(guard.x, 4)
        self.assertEqual(guard.y, 5)

    def test_turns_at_obstacle(self):
        layout = read_file("06/data/example.txt")
        area = [list(s) for s in layout]
        guard = Guard(area)
        for _ in range(10):
            guard.walk_forward()
        self.assertEqual(guard.x, 8)
        self.assertEqual(guard.y, 1)

    def test_part_one(self):
        received = part_one("06/data/example.txt")
        self.assertEqual(received, 41)

    def test_part_two(self):
        received = part_two("06/data/example.txt")
        self.assertEqual(received, 6)
