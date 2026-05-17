# Problem 225: https://projecteuler.net/problem=225
TARGET = 124


def never_divides(m):
    a = b = c = 1 % m
    start = (a, b, c)

    while True:
        a, b, c = b, c, (a + b + c) % m
        if c == 0:
            return False
        if (a, b, c) == start:
            return True


def solve():
    found = 0
    n = 1
    while found < TARGET:
        if never_divides(n):
            found += 1
        n += 2
    return n - 2


if __name__ == "__main__":
    print(solve())
