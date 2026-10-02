# Problem 650: https://projecteuler.net/problem=650

from sympy import factorint


def solve(limit=20_000):
    mod = 1_000_000_007
    powers = {}
    denominator = 1
    total = 0

    for n in range(1, limit + 1):
        for p, a in factorint(n).items():
            if p not in powers:
                powers[p] = [p, 1]
                denominator = denominator * pow(p - 1, -1, mod) % mod
            powers[p][0] = powers[p][0] * pow(p, n * a, mod) % mod
            powers[p][1] = powers[p][1] * pow(p, -a, mod) % mod

        d = 1
        for state in powers.values():
            state[0] = state[0] * state[1] % mod
            d = d * (state[0] - 1) % mod
        total = (total + d * denominator) % mod

    return total


if __name__ == "__main__":
    print(solve())
