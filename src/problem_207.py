# Problem 207: https://projecteuler.net/problem=207


def solve():
    for e in range(1, 100):
        n = max(1 << e, 12_345 * e + 2)
        if n < 1 << (e + 1):
            return n * (n - 1)


if __name__ == "__main__":
    print(solve())
