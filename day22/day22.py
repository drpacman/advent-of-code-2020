def read_decks(file):
    cards = [[], []]
    with open(file) as f:
        player = None
        for line in f.readlines():
            if len(line.strip()) == 0:
                continue
            if line.strip() == "Player 1:":
                player = 1
            elif line.strip() == "Player 2:":
                player = 2
            else:
                cards[player-1].append(int(line.strip()))
    return cards


def play_combat(decks):
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        if decks[0][0] > decks[1][0]:
            # print(f"Player 1 wins {decks[0][0]} beats {decks[1][0]}")
            decks[0] = decks[0][1:] + [decks[0][0]] + [decks[1][0]]
            decks[1] = decks[1][1:]
        else:
            # print(f"Player 2 wins {decks[1][0]} beats {decks[0][0]}")
            decks[1] = decks[1][1:] + [decks[1][0]] + [decks[0][0]]
            decks[0] = decks[0][1:]
    return decks


def play_recursive_combat(decks, game_number=1):
    round = 1
    previous = []
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        winner = -1
        # check for previous occurance
        if (decks[0] in [deck[0] for deck in previous]) or (decks[1] in [deck[1] for deck in previous]):
            return [decks[0], []]

        card1 = decks[0][0]
        card2 = decks[1][0]
        # print(f"Player 1's deck {decks[0]}\nPlayer 2's deck {decks[1]}\nPlayer 1 plays {card1}\nPlayer 2 plays {card2}")
        if card1 < len(decks[0]) and card2 < len(decks[1]):
            result = play_recursive_combat(
                [decks[0][1:card1+1], decks[1][1:card2+1]], game_number+1)
            winner = 0 if len(result[0]) > 0 else 1
        elif card1 > card2:
            winner = 0
        else:
            winner = 1

        # print(f"Player {winner+1} wins round {round} in Game {game_number}\n")
        previous.append(list([deck[:] for deck in decks]))
        if winner == 0:
            decks[0] = decks[0][1:] + [card1, card2]
            decks[1] = decks[1][1:]
        else:
            decks[1] = decks[1][1:] + [card2, card1]
            decks[0] = decks[0][1:]
        round = round + 1

    return decks


def calculate_score(decks):
    winning_deck = decks[0] if len(decks[0]) > 0 else decks[1]
    winning_deck.reverse()
    result = 0
    for index, card in enumerate(winning_deck):
        result = result + (index + 1) * card
    return result


decks = read_decks('input.txt')
result = play_combat(decks)
part1 = calculate_score(result)
print(f"Part1 - {part1}")

decks = read_decks('input.txt')
result = play_recursive_combat(decks)
part2 = calculate_score(result)
print(f"Part2 - {part2}")
