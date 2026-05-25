# Problem 254: https://projecteuler.net/problem=254
from math import factorial


N = 150
F = factorial(9)
FAC = [factorial(i) for i in range(10)]


def residue_data():
    length = [0] * F
    digitsum = [0] * F
    lex = [0] * F

    for r in range(F):
        x = r
        counts = [0] * 9
        for d in range(8, 0, -1):
            counts[d] = x // FAC[d]
            x %= FAC[d]

        length[r] = sum(counts)
        digitsum[r] = sum(d * counts[d] for d in range(1, 9))

        for d in range(1, 9):
            lex[r] = 10 * lex[r] + counts[d]

    return length, digitsum, lex


LENGTH, DIGITSUM, LEX = residue_data()


def first_with_digit_sum(s):
    q, r = divmod(s - 1, 9)
    return (r + 1) * 10**q + 10**q - 1


def sg(s):
    lo = first_with_digit_sum(s)
    r = lo % F
    hi = lo + F * LENGTH[r] - r
    low = list(map(int, str(lo).zfill(len(str(hi)))))
    high = list(map(int, str(hi)))
    n = len(high)
    best_len = 10**30
    best_lex = -1
    best = 0

    def test(m):
        nonlocal best_len, best_lex, best
        q, r = divmod(m, F)
        length = q + LENGTH[r]
        if length < best_len or (length == best_len and LEX[r] > best_lex):
            best_len = length
            best_lex = LEX[r]
            best = DIGITSUM[r] + 9 * q

    def visit(pos, rem, value, tight_low, tight_high):
        if pos == n:
            if rem == 0:
                test(value)
            return

        left = n - pos - 1
        a = low[pos] if tight_low else 0
        b = high[pos] if tight_high else 9
        a = max(a, rem - 9 * left)
        b = min(b, rem)

        for d in range(a, b + 1):
            visit(
                pos + 1,
                rem - d,
                10 * value + d,
                tight_low and d == low[pos],
                tight_high and d == high[pos],
            )

    visit(0, s, 0, True, True)
    return best


def solve():
    return sum(sg(i) for i in range(1, N + 1))


if __name__ == "__main__":
    print(solve())
