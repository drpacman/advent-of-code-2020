from functools import reduce

def parse(str, operator_precedence):
    result, _ = parse_tokens(tokenize(str), operator_precedence)
    return result

def tokenize(input):
    prepared = input.replace(' ', '')
    return [token for token in prepared]

def parse_tokens(tokens, operator_precedence):
    all_operators = [ op for operators in operator_precedence for op in operators  ] 
    local_tokens = []
    while len(tokens) > 0:
        token = tokens[0]
        tokens = tokens[1:]
        if token == '(':
            value, tokens = parse_tokens(tokens, operator_precedence)
            local_tokens.append(value)
        elif token == ')':
            break
        elif token in all_operators:
            local_tokens.append(token)
        else:
            local_tokens.append(int(token))
        
    for operators in operator_precedence:
        next_tokens = []
        while len(local_tokens) > 0:            
            token = local_tokens[0]
            local_tokens = local_tokens[1:]
            if token in operators:
                if token == '+':
                    value = next_tokens[-1] + local_tokens[0]
                elif token == '*':
                    value = next_tokens[-1] * local_tokens[0]
                next_tokens = next_tokens[:-1] + [value]
                local_tokens = local_tokens[1:]
            else:
                next_tokens.append(token)
        local_tokens = next_tokens
    
    return local_tokens[0], tokens

def get_result(operator_precedence):
    with open('input.txt') as file:
        values = [parse(line.strip(), operator_precedence) for line in file.readlines()]
        return reduce(lambda acc, x: acc + x, values, 0)

if __name__ == '__main__':
    part1 = get_result([['+', '*']])
    print(f"Part 1 - {part1}")
    part2 = get_result([['+'], ['*']])
    print(f"Part 2 - {part2}")
