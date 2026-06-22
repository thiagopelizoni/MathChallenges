# Problem 321: https://projecteuler.net/problem=321

TERMS = 40


def advance(x, a):
    return 3 * x + 8 * a, x + 3 * a


def solve():
    seq = [[5, 2], [11, 4]]
    total = 0

    for _ in range(TERMS):
        j = 0 if seq[0][1] < seq[1][1] else 1
        x, a = seq[j]
        total += a - 1
        seq[j] = list(advance(x, a))

    return total


if __name__ == "__main__":
    print(solve())
