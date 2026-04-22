# Problem 94: https://projecteuler.net/problem=94

def solve():
    lim = 1_000_000_000
    total = 0
    x, y = 4, 2

    while True:
        x, y = 2 * x + 3 * y, x + 2 * y
        p = x - 2 if x % 3 == 1 else x + 2

        if p > lim:
            return total

        total += p


if __name__ == "__main__":
    print(solve())
