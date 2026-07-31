# Problem 480: https://projecteuler.net/problem=480

from collections import Counter
from functools import cache
from math import comb


PHRASE = "thereisasyetinsufficientdataforameaningfulanswer"
LIMIT = 15
SUPPLY = Counter(PHRASE)
LETTERS = tuple(sorted(SUPPLY))
COUNTS = tuple(SUPPLY[letter] for letter in LETTERS)


@cache
def suffix_count(counts, limit):
    dp = [1] + [0] * limit
    for copies in counts:
        nxt = [0] * (limit + 1)
        for used, ways in enumerate(dp):
            if ways:
                for take in range(min(copies, limit - used) + 1):
                    nxt[used + take] += ways * comb(used + take, take)
        dp = nxt
    return sum(dp)


def rank(word):
    remaining = list(COUNTS)
    position = 0

    for length, letter in enumerate(word, 1):
        index = LETTERS.index(letter)
        for i in range(index):
            if remaining[i]:
                remaining[i] -= 1
                position += suffix_count(tuple(remaining), LIMIT - length)
                remaining[i] += 1
        remaining[index] -= 1
        position += 1

    return position


def unrank(position):
    remaining = list(COUNTS)
    word = []

    for length in range(1, LIMIT + 1):
        for i, letter in enumerate(LETTERS):
            if not remaining[i]:
                continue
            remaining[i] -= 1
            block = suffix_count(tuple(remaining), LIMIT - length)
            if position > block:
                position -= block
                remaining[i] += 1
                continue
            word.append(letter)
            if position == 1:
                return "".join(word)
            position -= 1
            break


def solve():
    position = (
        rank("legionary")
        + rank("calorimeters")
        - rank("annihilate")
        + rank("orchestrated")
        - rank("fluttering")
    )
    return unrank(position)


if __name__ == "__main__":
    print(solve())
