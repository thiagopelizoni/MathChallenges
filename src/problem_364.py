# Problem 364: https://projecteuler.net/problem=364


N = 1_000_000
MOD = 100_000_007


def factorial_tables(limit):
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = fact[i - 1] * i % MOD

    invfact = [1] * (limit + 1)
    invfact[limit] = pow(fact[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    return fact, invfact


def choose(n, r, fact, invfact):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD


def solve():
    fact, invfact = factorial_tables(N // 2 + 2)
    powers = [1] * (N // 3 + 4)
    for a in range(1, len(powers)):
        powers[a] = powers[a - 1] * 2 % MOD

    total = 0
    for b in range(3):
        end_gaps = choose(2, b, fact, invfact)
        for a in range((N - b - 1) // 3 + 1):
            rem = N - a - b + 1
            if rem % 2:
                continue

            k = rem // 2
            term = end_gaps * choose(k - 1, a, fact, invfact) % MOD
            term = term * fact[k] % MOD
            term = term * fact[a + b] % MOD
            term = term * fact[k - 1] % MOD
            term = term * powers[a] % MOD
            total = (total + term) % MOD

    return total


if __name__ == "__main__":
    print(solve())
