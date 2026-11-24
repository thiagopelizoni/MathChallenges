# Problem 796: https://projecteuler.net/problem=796

from fractions import Fraction
from math import comb


def solve():
    ranks, suits, decks, jokers = 13, 4, 10, 2
    total = decks * (ranks * suits + jokers)
    expected = Fraction()
    for r in range(ranks + 1):
        for s in range(suits + 1):
            per_deck = (ranks - r) * (suits - s) + jokers
            for d in range(decks + 1):
                selected = r + s + d
                if selected == 0:
                    continue
                matches = total - (decks - d) * per_deck
                ways = comb(ranks, r) * comb(suits, s) * comb(decks, d)
                term = Fraction(ways * (total + 1), matches + 1)
                expected += term if selected % 2 else -term
    return f"{float(expected):.8f}"


if __name__ == "__main__":
    print(solve())
