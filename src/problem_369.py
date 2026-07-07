# Problem 369: https://projecteuler.net/problem=369

from collections import defaultdict
from itertools import combinations
from math import comb


RANKS = 13
LIMIT = 13
SUITS = tuple(range(4))
FULL = SUITS
CHOICES = [tuple(c) for r in range(5) for c in combinations(SUITS, r)]
START = frozenset({()})


def add_suit(matched, suit):
    return tuple(sorted(matched + (suit,)))


def advance(state, choice):
    out = set(state)
    for matched in state:
        for suit in choice:
            if suit not in matched:
                out.add(add_suit(matched, suit))
    if FULL in out:
        return None
    return frozenset(out)


def no_badugi_counts():
    trans = {}
    dp = {(START, 0): 1}

    for _ in range(RANKS):
        ndp = defaultdict(int)
        for (state, cards), count in dp.items():
            for choice in CHOICES:
                nc = cards + len(choice)
                if nc > LIMIT:
                    continue

                key = state, choice
                if key not in trans:
                    trans[key] = advance(state, choice)
                nxt = trans[key]
                if nxt is not None:
                    ndp[nxt, nc] += count
        dp = ndp

    totals = [0] * (LIMIT + 1)
    for (_, cards), count in dp.items():
        totals[cards] += count
    return totals


def solve():
    no_badugi = no_badugi_counts()
    return sum(comb(52, n) - no_badugi[n] for n in range(4, LIMIT + 1))


if __name__ == "__main__":
    print(solve())
