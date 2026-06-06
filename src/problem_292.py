# Problem 292: https://projecteuler.net/problem=292

from math import gcd, isqrt


PERIMETER = 120
SPAN = 2 * PERIMETER + 1
LAYER = SPAN * SPAN


def state(x, y, p):
    return p * LAYER + (x + PERIMETER) * SPAN + (y + PERIMETER)


def edge_groups(limit):
    by_direction = {}
    opposite_edges = 0

    for x in range(-limit, limit + 1):
        x2 = x * x
        for y in range(-limit, limit + 1):
            if x == 0 and y == 0:
                continue

            sq = x2 + y * y
            length = isqrt(sq)
            if length * length != sq or length > limit:
                continue

            if 2 * length <= limit:
                opposite_edges += 1

            g = gcd(abs(x), abs(y))
            direction = (x // g, y // g)
            delta = length * LAYER + x * SPAN + y
            by_direction.setdefault(direction, []).append((length, delta))

    return [sorted(by_direction[k]) for k in sorted(by_direction)], opposite_edges // 2


def count(limit):
    groups, opposite_pairs = edge_groups(limit)
    ways = {state(0, 0, 0): 1}

    for group in groups:
        nxt = ways.copy()
        get = nxt.get
        for k, nways in ways.items():
            left = limit - k // LAYER
            for length, delta in group:
                if length > left:
                    break
                nk = k + delta
                nxt[nk] = get(nk, 0) + nways
        ways = nxt

    closed = sum(ways.get(state(0, 0, p), 0) for p in range(limit + 1))
    return closed - 1 - opposite_pairs


def solve():
    return count(PERIMETER)


if __name__ == "__main__":
    print(solve())
