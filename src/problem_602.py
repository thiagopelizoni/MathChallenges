# Problem 602: https://projecteuler.net/problem=602


def solve(n=10_000_000, k=4_000_000):
    mod = 10**9 + 7
    total = pow(k, n, mod)
    coefficient = 1
    for j in range(1, k + 1):
        coefficient = -coefficient * (n + 2 - j) * pow(j, -1, mod) % mod
        total = (total + coefficient * pow(k - j, n, mod)) % mod
    return total


if __name__ == "__main__":
    print(solve())
