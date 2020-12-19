import unittest
import day18

class Day18Test(unittest.TestCase):

    part1 = [['+', '*']]
    part2 = [['+'], ['*']]
    
    def test_parse(self):
        result = day18.parse('1 + 2 * 3 + 4 * 5 + 6', self.part1)
        assert(result == 71)
    
    def test_parse_brackets(self):
        result = day18.parse('2 * 3 + (4 * 5)', self.part1)
        assert(result == 26)

    def test_many_brackets(self):
        result = day18.parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', self.part1)
        assert(result == 13632)
    
    def test_many_brackets_second_example(self):
        result = day18.parse('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', self.part1)
        assert(result == 12240)

    def test_part2_example(self):
        result = day18.parse('1 + 2 * 3 + 4 * 5 + 6', self.part2)
        assert(result == 231)
    
    def test_part2_many_brackets_second_example(self):
        result = day18.parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', self.part2)
        print(result)
        assert(result == 23340)
    
if __name__ == '__main__':
    unittest.main()