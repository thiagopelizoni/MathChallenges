# Problem 555: https://projecteuler.net/problem=555


LIMIT = 1_000_000


def solve():
    total = 0
    for d in range(1, LIMIT // 2 + 1):
        count = LIMIT // d - 1
        total += d * count * (2 * LIMIT + 1 - d * count) // 2
    return total


if __name__ == "__main__":
    print(solve())
