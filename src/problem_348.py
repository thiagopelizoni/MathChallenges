# Problem 348: https://projecteuler.net/problem=348

from math import isqrt


TARGET = 5


def palindromes():
    d = 2

    while True:
        h = (d + 1) // 2
        for x in range(10 ** (h - 1), 10**h):
            s = str(x)
            if d % 2:
                yield int(s + s[-2::-1])
            else:
                yield int(s + s[::-1])
        d += 1


def count_ways(n):
    cnt = 0
    b = 2

    while b**3 < n - 1:
        a2 = n - b**3
        a = isqrt(a2)
        if a > 1 and a * a == a2:
            cnt += 1
            if cnt > 4:
                break
        b += 1

    return cnt


def solve():
    found = []

    for n in palindromes():
        if count_ways(n) == 4:
            found.append(n)
            if len(found) == TARGET:
                return sum(found)


if __name__ == "__main__":
    print(solve())
