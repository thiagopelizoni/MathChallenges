# Problem 520: https://projecteuler.net/problem=520

from collections import defaultdict

MOD = 1_000_000_123
HALF = pow(2, -1, MOD)
ODD = ((0, 1), (1, HALF), (-1, -HALF))
EVEN = ((1, HALF), (-1, HALF))
ODD_PARITY = ((1, HALF), (-1, -HALF))


def spectrum(factors):
    values = {0: 1}
    for factor in factors:
        next_values = defaultdict(int)
        for base, coefficient in values.items():
            for term, weight in factor:
                next_values[base + term] = (
                    next_values[base + term] + coefficient * weight
                ) % MOD
        values = next_values
    return values


def geometric_sum(base, n):
    base %= MOD
    if base == 1:
        return n % MOD
    return (pow(base, n, MOD) - 1) * pow(base - 1, -1, MOD) % MOD


def solve():
    all_digits = spectrum([ODD] * 5 + [EVEN] * 5)
    leading_zero = spectrum([ODD] * 5 + [ODD_PARITY] + [EVEN] * 4)

    total = 0
    for u in range(1, 40):
        n = 2**u
        for base, coefficient in all_digits.items():
            total += (
                coefficient * base - leading_zero[base]
            ) * geometric_sum(base, n)
    return total % MOD


if __name__ == "__main__":
    print(solve())
