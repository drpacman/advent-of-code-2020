import unittest
import day24

class TestDay24(unittest.TestCase):
    def test_parse(self):
        sequence = day24.split_input('esew')
        self.assertEqual(sequence, ['e', 'se', 'w'])

    def test_flip_example1(self):
        tiles = day24.process([['e','se','w']])
        self.assertEqual(len(tiles), 1)

    def test_flip_example_input(self):
        sequence = day24.read_input('input.test.txt')
        self.assertEqual(len(day24.process(sequence)), 10)

    def test_day_flip(self):
        sequence = day24.read_input('input.test.txt')
        day0 = day24.process(sequence)
        day1 = day24.apply_end_of_day_rules(day0)
        self.assertEqual(len(day1), 15)

if __name__ == '__main__':
    unittest.main()