# Problem 713: https://projecteuler.net/problem=713


def solve(n=10**7):
    total = 0
    for k in range(1, n):
        q, r = divmod(n, k)
        total += k * q * (q - 1) // 2 + r * q
    return total


if __name__ == "__main__":
    print(solve())
