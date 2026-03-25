# Problem 49: https://projecteuler.net/problem=49
from collections import defaultdict
from itertools import combinations
from gmpy2 import is_prime

def solve():
    groups = defaultdict(list)
    for p in range(1000, 10000):
        if not is_prime(p):
            continue
        groups["".join(sorted(str(p)))].append(p)

    for values in groups.values():
        if len(values) < 3:
            continue
        s = set(values)
        for a, b in combinations(values, 2):
            c = 2 * b - a
            if c in s and a != 1487:
                return int(f"{a}{b}{c}")

if __name__ == "__main__":
    print(solve())