from collections import Counter
from functools import cmp_to_key

def get_card_ranks(part2=False):
    if part2:
        return {
            'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7,
            '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1
        }
    else:
        return {
            'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8,
            '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
        }

def hand_type(hand):
    counts = Counter(hand)
    if len(counts) == 1:
        return 7  # Five of a kind
    elif len(counts) == 2:
        if 4 in counts.values():
            return 6  # Four of a kind
        return 5  # Full house
    elif len(counts) == 3:
        if 3 in counts.values():
            return 4  # Three of a kind
        return 3  # Two pair
    elif len(counts) == 4:
        return 2  # One pair
    return 1  # High card

def compare_hands(hand1, hand2):
    card_ranks = get_card_ranks()
    type1 = hand_type(hand1[0])
    type2 = hand_type(hand2[0])
    
    if type1 != type2:
        return type1 - type2
    
    for c1, c2 in zip(hand1[0], hand2[0]):
        if c1 != c2:
            return card_ranks[c1] - card_ranks[c2]
    
    return 0

def calculate_winnings(hands_and_bids):
    sorted_hands = sorted(hands_and_bids, key=cmp_to_key(compare_hands))
    
    total_winnings = 0
    for rank, (hand, bid) in enumerate(sorted_hands, 1):
        total_winnings += rank * bid
    
    return total_winnings


def hand_type_part2(hand):
    counts = Counter(hand)
    joker_count = counts.pop('J', 0)
    
    if joker_count == 5 or joker_count == 4:
        return 7  # Five of a kind
    
    if counts:
        most_common = max(counts, key=counts.get)
        counts[most_common] += joker_count
    else:
        return 7  # All jokers, five of a kind
    
    if 5 in counts.values():
        return 7  # Five of a kind
    elif 4 in counts.values():
        return 6  # Four of a kind
    elif 3 in counts.values() and 2 in counts.values():
        return 5  # Full house
    elif 3 in counts.values():
        return 4  # Three of a kind
    elif list(counts.values()).count(2) == 2:
        return 3  # Two pair
    elif 2 in counts.values():
        return 2  # One pair
    return 1  # High card

def compare_hands_part2(hand1, hand2):
    card_ranks = get_card_ranks(part2=True)
    type1 = hand_type_part2(hand1[0])
    type2 = hand_type_part2(hand2[0])
    
    if type1 != type2:
        return type1 - type2
    
    for c1, c2 in zip(hand1[0], hand2[0]):
        if c1 != c2:
            return card_ranks[c1] - card_ranks[c2]
    
    return 0

def calculate_winnings_part2(hands_and_bids):
    sorted_hands = sorted(hands_and_bids, key=cmp_to_key(compare_hands_part2))
    
    total_winnings = 0
    for rank, (hand, bid) in enumerate(sorted_hands, 1):
        total_winnings += rank * bid
    
    return total_winnings

def read_input_file(file_path):
    hands_and_bids = []
    with open(file_path, 'r') as f:
        for line in f:
            hand, bid = line.strip().split()
            hands_and_bids.append((hand, int(bid)))
    return hands_and_bids

def main():
    input_file = 'input.txt'
    hands_and_bids = read_input_file(input_file)
    
    
    total_winnings_part1 = calculate_winnings(hands_and_bids)
    print(f"Part 1 - Total winnings: {total_winnings_part1}")
    
    
    total_winnings_part2 = calculate_winnings_part2(hands_and_bids)
    print(f"Part 2 - Total winnings with joker rule: {total_winnings_part2}")

if __name__ == "__main__":
    main()