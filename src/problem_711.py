# Problem 711: https://projecteuler.net/problem=711


def solve(n=12_345_678):
    mod = 1_000_000_007
    inv = pow(3, -1, mod)
    k = (n - 1) // 2
    count = pow(2, k, mod)
    total = count * (4 * (pow(4, k, mod) - 1) * inv - 1) + 1
    if n % 2 == 0:
        total += 2 * pow(2, n, mod) - 1
    k = (n + 1) // 2
    total += 2 * (pow(4, k, mod) - 1) * inv - k
    return total % mod


if __name__ == "__main__":
    print(solve())
