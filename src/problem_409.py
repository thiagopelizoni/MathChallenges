# Problem 409: https://projecteuler.net/problem=409

MOD = 1_000_000_007
N = 10_000_000
INVERSE_2 = pow(2, -1, MOD)


def binomial_lucas(top, k):
    top %= MOD
    numerator = factorial = 1

    for i in range(1, k + 1):
        factorial = factorial * i % MOD
        if top >= k:
            numerator = numerator * (top - k + i) % MOD

    value = numerator * pow(factorial, -1, MOD) % MOD if top >= k else 0
    return value, factorial


def winning_positions(n):
    power = pow(2, n, MOD)
    total, orderings = binomial_lucas(power - 1, n)
    half, _ = binomial_lucas((power * INVERSE_2 - 1) % MOD, n // 2)
    coefficient = half if (n + 1) // 2 % 2 == 0 else -half
    unordered = (power - 1) * (total - coefficient) % MOD
    unordered = unordered * pow(power, -1, MOD) % MOD
    return unordered * orderings % MOD


def solve():
    return winning_positions(N)


if __name__ == "__main__":
    print(solve())
