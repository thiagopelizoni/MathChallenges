# Problem 98: https://projecteuler.net/problem=98

from collections import defaultdict
from csv import reader
from itertools import combinations
from itertools import permutations
from math import isqrt
from urllib.request import urlopen


WORDS_URL = "https://projecteuler.net/resources/documents/0098_words.txt"


def anagrams():
    with urlopen(WORDS_URL) as res:
        words = next(reader([res.read().decode()]))

    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)

    return [group for group in groups.values() if len(group) > 1]


def square_map(word, n):
    digits = str(n)
    mp = {}
    used = set()

    for c, d in zip(word, digits):
        if c in mp:
            if mp[c] != d:
                return None
        elif d in used:
            return None
        else:
            mp[c] = d
            used.add(d)

    return mp


def apply_map(word, mp):
    if mp[word[0]] == "0":
        return None
    return int("".join(mp[c] for c in word))


def solve():
    squares = {}
    groups = anagrams()

    for n in {len(group[0]) for group in groups}:
        lo = isqrt(10 ** (n - 1) - 1) + 1
        hi = isqrt(10**n - 1)
        squares[n] = {k * k for k in range(lo, hi + 1)}

    ans = 0
    for group in groups:
        n = len(group[0])
        for pair in combinations(group, 2):
            for a, b in permutations(pair):
                for sq in squares[n]:
                    mp = square_map(a, sq)
                    if mp is None:
                        continue
                    other = apply_map(b, mp)
                    if other in squares[n]:
                        ans = max(ans, sq, other)

    return ans


if __name__ == "__main__":
    print(solve())
