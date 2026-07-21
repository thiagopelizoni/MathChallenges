# Problem 422: https://projecteuler.net/problem=422

MOD = 1_000_000_007
N = 11**14


def fibonacci_pair(n, mod):
    if n == 0:
        return 0, 1
    a, b = fibonacci_pair(n // 2, mod)
    c = a * (2 * b - a) % mod
    d = (a * a + b * b) % mod
    return (d, (c + d) % mod) if n % 2 else (c, d)


def solve():
    f, next_f = fibonacci_pair(N - 1, MOD - 1)
    lucas = (2 * next_f - f) % (MOD - 1)
    two = pow(2, lucas, MOD)
    three = pow(3, f, MOD)

    a = (3 * two * two + 4 * three * three) * pow(12, -1, MOD) % MOD
    b = pow(2, lucas - 2, MOD) * pow(3, f - 1, MOD) % MOD
    c = (4 * two * two - 3 * three * three) % MOD
    d = two * three % MOD
    return (a + b + c + d) % MOD


if __name__ == "__main__":
    print(solve())
