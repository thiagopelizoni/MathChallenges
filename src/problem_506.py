# Problem 506: https://projecteuler.net/problem=506

from itertools import cycle


MOD = 123_454_321
N = 10**14
DIGITS = (1, 2, 3, 4, 3, 2)


def initial_values():
    digits = cycle(DIGITS)
    values = []
    for n in range(1, 61):
        digit_sum = 0
        value = 0
        while digit_sum < n:
            digit = next(digits)
            digit_sum += digit
            value = 10 * value + digit
        values.append(value)
    return values


def geometric_sums(p, n):
    if n == 0:
        return 1, 0, 0
    if n % 2:
        power, total, prefixes = geometric_sums(p, n - 1)
        return (
            power * p % MOD,
            (total + power) % MOD,
            (prefixes + total) % MOD,
        )

    power, total, prefixes = geometric_sums(p, n // 2)
    return (
        power * power % MOD,
        total * (1 + power) % MOD,
        ((1 + power) * prefixes + n // 2 * total) % MOD,
    )


def summatory(n):
    values = initial_values()
    p = pow(10, 12, MOD)
    result = 0

    for residue in range(1, 31):
        if residue > n:
            break
        count = (n - residue) // 30 + 1
        constant = (values[residue + 29] - values[residue - 1] * 10**12) % MOD
        _, powers, prefix_sums = geometric_sums(p, count)
        result += values[residue - 1] * powers + constant * prefix_sums

    return result % MOD


def solve():
    return summatory(N)


if __name__ == "__main__":
    print(solve())
