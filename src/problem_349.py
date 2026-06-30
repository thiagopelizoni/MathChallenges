# Problem 349: https://projecteuler.net/problem=349


N = 10**18
TRANSIENT = 11_000
PERIOD = 104
GROWTH = 12
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def black_after(steps):
    black = set()
    x = y = d = 0

    for _ in range(steps):
        p = (x, y)
        if p in black:
            black.remove(p)
            d = (d - 1) % 4
        else:
            black.add(p)
            d = (d + 1) % 4

        dx, dy = DIRECTIONS[d]
        x += dx
        y += dy

    return len(black)


def solve():
    base = TRANSIENT + (N - TRANSIENT) % PERIOD
    return black_after(base) + (N - base) // PERIOD * GROWTH


if __name__ == "__main__":
    print(solve())
