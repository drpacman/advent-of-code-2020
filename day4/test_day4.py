import unittest
import day4

class MyModuleTest(unittest.TestCase):
    
    def test_parse_input(self):
        contents = day4.parse_file("input.test.txt")
        assert(len(contents)== 4)
        assert(contents[0]['byr'] == "1937")

    def test_valid_fields_present(self):
        contents = day4.parse_file("input.test.txt")
        assert(day4.valid_fields_present(contents[0]) == True)
        assert(day4.valid_fields_present(contents[1]) == False)
        assert(day4.valid_fields_present(contents[2]) == True)

    def test_byr_check(self):
        assert(day4.validate_byr("2002"))
        assert(day4.validate_byr("2003") == False)

    def test_pid_check(self):
        assert(day4.validate_pid("000000001"))
        assert(day4.validate_pid("0123456789") == False)

    def test_hcl_check(self):
        assert(day4.validate_hcl('#01010f'))
        assert(day4.validate_hcl('#01010') == False)
        assert(day4.validate_hcl('01010f') == False)
        assert(day4.validate_hcl('#123abz') == False)
    
    def test_hgt_check(self):
        assert(day4.validate_hgt('190cm'))
        assert(day4.validate_hgt('190in') == False)
        assert(day4.validate_hgt('190') == False)

    def test_ecl_check(self):
        assert(day4.validate_ecl('brn'))
        assert(day4.validate_ecl('wat') == False)
    
    def test_invalid_passport(self):
        contents = day4.parse_file("input.invalid.txt")    
        assert(len(day4.validate_passports(contents)) == 0)
    
    def test_valid_passport(self):
        contents = day4.parse_file("input.valid.txt")        
        assert(len(day4.validate_passports(contents)) == 4)
    
if __name__ == '__main__':
    unittest.main()