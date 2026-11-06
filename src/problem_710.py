# Problem 710: https://projecteuler.net/problem=710


def solve():
    mod = 1_000_000
    a, b = 0, 1
    total = 1
    power = 1
    n = 0

    while True:
        n += 2
        c = (total - a) % mod
        total = (total + c) % mod
        power = 2 * power % mod

        t = (power - total + b) % mod
        if n > 42 and t == 0:
            return n

        t = (power - total) % mod
        if n + 1 > 42 and t == 0:
            return n + 1

        a, b = b, c


if __name__ == "__main__":
    print(solve())
