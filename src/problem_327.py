# Problem 327: https://projecteuler.net/problem=327

R = 30


def m(c, r):
    cards = 2

    for _ in range(2, r + 1):
        cards += 1 + 2 * ((cards - 2) // (c - 2))

    return cards


def solve():
    return sum(m(c, R) for c in range(3, 41))


if __name__ == "__main__":
    print(solve())
