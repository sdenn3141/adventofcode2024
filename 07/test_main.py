import unittest
from .main import SolutionFinder
from helpers import read_file

example_file_path = "07/example.txt"

class TestPartSeven(unittest.TestCase):
  def setUp(self):
    self.solution_finder = SolutionFinder(['*', '+'])
    self.concat_solution_finder = SolutionFinder(['*', '+', '||'])

  def test_solution_row(self):
    contents = read_file(example_file_path)
    row = contents[0]
    expected = self.solution_finder.calc_row(row)
    self.assertEqual(expected, 190)
  
  def test_no_solution_row(self):
    contents = read_file(example_file_path)
    row = contents[2]
    expected = self.solution_finder.calc_row(row)
    self.assertEqual(expected, 0)
  
  def test_solution_row_multiple_symbols(self):
    contents = read_file(example_file_path)
    row = contents[-1]
    expected = self.solution_finder.calc_row(row)
    self.assertEqual(expected, 292)

  def test_full_example(self):
    total = 0
    for row in read_file(example_file_path):
      total += self.solution_finder.calc_row(row)
    self.assertEqual(total, 3749)

  def test_solution_row_with_concat_operator(self):
    contents = read_file(example_file_path)
    row = contents[6]
    expected = self.solution_finder.calc_row(row)
    self.assertEqual(expected, 0)
    expected = self.concat_solution_finder.calc_row(row)
    self.assertEqual(expected, 192)

  def test_full_example_with_concat_operator(self):
    total = 0
    for row in read_file(example_file_path):
      total += self.concat_solution_finder.calc_row(row)
    self.assertEqual(total, 11387)
  
  def test_unsupported_operator(self):
    contents = read_file(example_file_path)
    row = contents[0]
    solution_finder = SolutionFinder(['-'])
    with self.assertRaises(ValueError) as context:
      solution_finder.calc_row(row)
    self.assertTrue('The operator: - is not supported' in str(context.exception))