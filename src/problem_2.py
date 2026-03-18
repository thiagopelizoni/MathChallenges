# Problem 2: https://projecteuler.net/problem=2
def solve():
    lim = 4_000_000
    total = 0
    a, b = 2, 8

    while a <= lim:
        total += a
        a, b = b, 4 * b + a

    return total


if __name__ == "__main__":
    print(solve())