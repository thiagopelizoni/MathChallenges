# Problem 698: https://projecteuler.net/problem=698

from functools import cache
from math import factorial


@cache
def valid(n):
    if n == 1:
        return True
    s = str(n)
    return all(d in "123" for d in s) and all(valid(s.count(d)) for d in set(s))


def solve(k=111_111_111_111_222_333):
    n = 0
    while True:
        n += 1
        counts = [0] + [i for i in range(1, n + 1) if valid(i)]
        allowed = set(counts)
        triples = []
        total = 0
        for a in counts:
            for b in counts:
                c = n - a - b
                if c in allowed:
                    triples.append((a, b, c))
                    total += factorial(n) // (factorial(a) * factorial(b) * factorial(c))
        if k <= total:
            break
        k -= total

    used = [0, 0, 0]
    ans = 0
    for pos in range(n):
        for digit in range(1, 4):
            used[digit - 1] += 1
            total = 0
            for a, b, c in triples:
                a -= used[0]
                b -= used[1]
                c -= used[2]
                if min(a, b, c) >= 0:
                    total += factorial(n - pos - 1) // (factorial(a) * factorial(b) * factorial(c))
            if k <= total:
                ans = (10 * ans + digit) % 123_123_123
                break
            k -= total
            used[digit - 1] -= 1
    return ans


if __name__ == "__main__":
    print(solve())
