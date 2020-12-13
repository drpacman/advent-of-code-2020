import unittest
import day13

class Day13Test(unittest.TestCase):
    def test_read_timetable(self):
        start_time, buses = day13.read_timetable('input.test.txt')
        assert(start_time == 939)
        assert(len(buses) == 5)

    def test_part1(self):
        start_time, buses = day13.read_timetable('input.test.txt')
        bus_number, wait_time = day13.pick_bus( start_time, buses )
        assert(bus_number == 59)
        assert(wait_time == 5)

    def test_read_bus_positions(self):
        buses = day13.read_bus_positions('input.test.txt')
        assert(buses[0] == 7)

    def test_find_timestamp(self):
        timestamp = day13.find_timestamp_chinese_remainders_with_sieve({0 : 17, 2 : 13, 3: 19})
        assert(timestamp == 3417)
        timestamp = day13.find_timestamp_chinese_remainders_with_sieve({ 0: 67, 1: 7, 3: 59, 4: 61})
        assert(timestamp == 1261476)
        timestamp = day13.find_timestamp_chinese_remainders_with_sieve({0: 1789, 1: 37, 2: 47,3 : 1889})
        assert(timestamp == 1202161486)
    
    def test_part2(self):
        buses = day13.read_bus_positions('input.test.txt')
        timestamp = day13.find_timestamp_chinese_remainders_with_sieve(buses)
        assert(timestamp == 1068781)

if __name__ == '__main__':
    unittest.main()
