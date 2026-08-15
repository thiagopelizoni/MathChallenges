# Problem 541: https://projecteuler.net/problem=541

from functools import cache

from sympy import summation, symbols


def maximum(p):
    x, end = symbols("x end", integer=True, nonnegative=True)

    digits = {}
    h = 0
    for a in range(p):
        if a:
            h = (h + pow(a, -1, p)) % p
        digits.setdefault(h, []).append(a)

    @cache
    def power_sum_formula(m):
        return summation(x**m, (x, 0, end - 1))

    @cache
    def power_sum(m, n):
        return int(power_sum_formula(m).subs(end, n))

    @cache
    def inverse_sums(s):
        mod = p**s
        return tuple(
            sum(pow(j, -m - 1, mod) for j in range(1, p)) % mod
            for m in range(s)
        )

    @cache
    def unit_sum(n, s):
        mod = p**s
        q, r = divmod(n, p)
        total = 0
        for m, c in enumerate(inverse_sums(s)):
            term = p**m * power_sum(m, q) * c
            total += -term if m % 2 else term
        total += sum(pow(q * p + j, -1, mod) for j in range(1, r + 1))
        return total % mod

    def value(e, n):
        s = e + 1
        mod = p**s
        total = 0
        coeff = p ** (e - 1)
        for _ in range(e):
            total += coeff * unit_sum(n, s)
            n //= p
            coeff //= p
        return total % mod

    best = p - 1
    candidates = digits[0][1:]
    e = 1

    while candidates:
        best = max(best, p * max(candidates) + p - 1)
        next_candidates = []
        pe = p**e
        for q in candidates:
            digit = value(e, q) // pe
            for a in digits.get(-digit % p, ()):
                next_candidates.append(q * p + a)
        candidates = next_candidates
        e += 1

    return best


def solve():
    return maximum(137)


if __name__ == "__main__":
    print(solve())
