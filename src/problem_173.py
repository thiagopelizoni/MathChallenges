# Problem 173: https://projecteuler.net/problem=173


def solve():
    total = 0
    tiles = 1_000_000
    t = 1

    while True:
        count = tiles // (4 * t) - t
        if count <= 0:
            return total
        total += count
        t += 1


if __name__ == "__main__":
    print(solve())
