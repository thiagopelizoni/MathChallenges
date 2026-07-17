# Problem 405: https://projecteuler.net/problem=405

MOD = 17**7
PHI = 16 * 17**6
K = 10**18
INVERSE_15 = pow(15, -1, MOD)


def tiling_points(n):
    sign = -1 if n % 2 else 1
    numerator = 6 * pow(4, n, MOD) - 20 * pow(2, n, MOD) + 15 - sign
    return numerator * INVERSE_15 % MOD


def solve():
    return tiling_points(pow(10, K, PHI))


if __name__ == "__main__":
    print(solve())
