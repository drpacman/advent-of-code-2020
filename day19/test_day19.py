import day19
import unittest


class Day19Test(unittest.TestCase):

    def test_parse_input(self):
        rules, entries = day19.read_input('input.test.txt')
        self.assertEqual(rules[4], [['a']])
        self.assertEqual(rules[3], [[4, 5], [5, 4]])
        self.assertEqual(entries[2], 'abbbab')

    def test_matches_rules(self):
        rules, _ = day19.read_input('input.test.txt')
        matcher = day19.matcher(rules)
        self.assertTrue(matcher('aaaabb'))
        self.assertFalse(matcher('aaaabbb'))

    def test_matches_rules_count_part2(self):
        rules, entries = day19.read_input('input.test2.txt')
        self.assertEqual(day19.count_matching_entries(rules, entries), 3)        

    def test_matches_rules_patched_count_part2(self):
        rules, entries = day19.read_input('input.test2.txt')
        rules = day19.patch_rules(rules)
        self.assertEqual(day19.count_matching_entries(rules, entries), 12)        

    def test_matches_rules_patched_elems_part2(self):
        rules, _ = day19.read_input('input.test2.txt')
        rules = day19.patch_rules(rules)
        matcher = day19.matcher(rules)
        self.assertFalse(matcher('aaaabbaaaabbaaa'))        
        self.assertTrue(matcher('aaaaabbaabaaaaababaa'))             

if __name__ == '__main__':
    unittest.main()