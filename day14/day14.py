import re


class Memory():

    def __init__(self, instructions):
        self.instructions = instructions
        self.memory = {}
        self.mask = 0

    def to_binary_array(self, n):
        value = [1 if digit == '1' else 0 for digit in bin(n)[2:]]
        prefix = [0] * (36 - len(value))
        return prefix + value

    def from_binary_array(self, array):
        value = 0
        n = 1
        array.reverse()
        for entry in array:
            value = value + (n if entry == 1 else 0)
            n = n << 1
        return value

    def run(self):

        for instruction in self.instructions:
            matches = re.match("mask = ([X01]+)", instruction)
            if matches:
                self.mask = matches[1]
            else:
                matches = re.match(r"mem\[([0-9]+)\] = ([0-9]+)", instruction)
                self.handle(matches[1], matches[2])

    def handle(self):
        pass

    def calculate_result(self):
        result = 0
        for key in self.memory.keys():
            result = result + self.memory[key]
        return result


class Part1(Memory):
    @staticmethod
    def load_from_file(file):
        with open(file) as f:
            return Part1(f.readlines())

    def handle(self, address, value):
        address = int(address)
        binary = self.to_binary_array(int(value))
        result = [0] * 36
        for index, char in enumerate(self.mask):
            if char == 'X':
                result[index] = binary[index]
            else:
                result[index] = int(char)
        self.memory[address] = self.from_binary_array(result)


class Part2(Memory):

    @staticmethod
    def load_from_file(file):
        with open(file) as f:
            return Part2(f.readlines())

    def append_value_to_answers(self, value, answers):
        result = []
        for answer in answers:
            a = answer.copy()
            a.append(value)
            result.append(a)
        return result

    def get_addresses(self, masked_input, answers=[[]]):
        if len(masked_input) == 0:
            return answers
        head = masked_input[0]
        tail = masked_input[1:]
        if masked_input[0] == 'X':
            result = []
            for val in [0, 1]:
                result = result + \
                    self.get_addresses(
                        tail, self.append_value_to_answers(val, answers))
            return result
        else:
            return self.get_addresses(tail, self.append_value_to_answers(head, answers))

    def handle(self, address, value):
        binary = self.to_binary_array(int(address))
        result = [0] * 36
        for index, char in enumerate(self.mask):
            if char == 'X':
                result[index] = 'X'
            elif char == '0':
                result[index] = binary[index]
            else:
                result[index] = 1

        for address in self.get_addresses(result):
            location = self.from_binary_array(address)
            self.memory[location] = int(value)


m = Part1.load_from_file('input.txt')
m.run()
part1 = m.calculate_result()
print(f"Part 1 - {part1}")

m = Part2.load_from_file('input.txt')
m.run()
part2 = m.calculate_result()
print(f"Part 2 - {part2}")
