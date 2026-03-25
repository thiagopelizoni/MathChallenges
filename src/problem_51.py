# Problem 51: https://projecteuler.net/problem=51
from itertools import combinations
from gmpy2 import is_prime, next_prime

def family(s, idx):
    values = []
    for d in "0123456789":
        if idx[0] == 0 and d == "0":
            continue
        t = list(s)
        for i in idx:
            t[i] = d
        n = int("".join(t))
        if is_prime(n):
            values.append(n)
    return values

def solve():
    p = 11
    while True:
        p = int(next_prime(p))
        s = str(p)
        for d in "0123456789":
            pos = [i for i, ch in enumerate(s[:-1]) if ch == d]
            for r in range(1, len(pos) + 1):
                for idx in combinations(pos, r):
                    values = family(s, idx)
                    if len(values) == 8:
                        return values[0]

if __name__ == "__main__":
    print(solve())