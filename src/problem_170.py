# Problem 170: https://projecteuler.net/problem=170
from functools import cache
from itertools import permutations
from math import gcd

FULL = (1 << 10) - 1


def digit_mask(s):
    mask = 0
    for ch in s:
        bit = 1 << (ord(ch) - 48)
        if mask & bit:
            return -1
        mask |= bit
    return mask


TWO_DIGIT = [n for n in range(10, 99) if digit_mask(str(n)) >= 0]


def two_digit_multiplier(s):
    for cut in range(1, 10):
        if s[0] == "0" and cut > 1:
            continue
        if s[cut] == "0" and cut < 9:
            continue

        a = int(s[:cut])
        b = int(s[cut:])
        g = gcd(a, b)

        for m in TWO_DIGIT:
            if m > g:
                break
            if g % m:
                continue
            x, y = a // m, b // m
            if x and y and digit_mask(str(m) + str(x) + str(y)) == FULL:
                return True
    return False


def one_digit_multiplier(s):
    for m in range(1, 10):
        start = 1 << m

        @cache
        def works(pos, mask, cnt, extra):
            if extra > 1:
                return False
            if pos == 10:
                return cnt >= 2 and extra == 1 and mask == FULL

            p = 0
            for end in range(pos + 1, 11):
                if s[pos] == "0" and end > pos + 1:
                    break
                p = 10 * p + ord(s[end - 1]) - 48
                if p % m:
                    continue
                q = p // m
                if q == 0:
                    continue
                qs = str(q)
                qmask = digit_mask(qs)
                if qmask >= 0 and not qmask & mask:
                    if works(end, mask | qmask, cnt + 1, extra + end - pos - len(qs)):
                        return True
            return False

        if works(0, start, 0, 0):
            return True
    return False


def solve():
    for p in permutations("9876543210"):
        s = "".join(p)
        if two_digit_multiplier(s) or one_digit_multiplier(s):
            return int(s)


if __name__ == "__main__":
    print(solve())
