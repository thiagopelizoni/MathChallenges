# Problem 479: https://projecteuler.net/problem=479


def solve():
    n = 10**6
    mod = 1_000_000_007
    total = 0

    for k in range(1, n + 1):
        q = (1 - k * k) % mod
        total += (q - pow(q, n + 1, mod)) * pow(k, -2, mod)

    return total % mod


if __name__ == "__main__":
    print(solve())
