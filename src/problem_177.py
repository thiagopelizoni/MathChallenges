# Problem 177: https://projecteuler.net/problem=177
from collections import defaultdict
from math import log, radians, sin

SCALE = 10**10


def canonical(angles):
    pairs = [angles[i:i + 2] for i in range(0, 8, 2)]
    forms = []

    for i in range(4):
        rotated = pairs[i:] + pairs[:i]
        forms.append(tuple(a for pair in rotated for a in pair))

    reflected = [(b, a) for a, b in pairs[::-1]]
    for i in range(4):
        rotated = reflected[i:] + reflected[:i]
        forms.append(tuple(a for pair in rotated for a in pair))

    return min(forms)


def log_ratios():
    vals = [[0.0] * 180 for _ in range(181)]
    for s in range(2, 179):
        for a in range(1, s):
            vals[s][a] = log(sin(radians(a))) - log(sin(radians(s - a)))
    return vals


def solve():
    vals = log_ratios()
    quadrilaterals = set()

    for x in range(2, 179):
        y = 180 - x
        buckets = defaultdict(list)

        for b in range(1, x):
            bx = vals[x][b]
            for d in range(1, y):
                buckets[round((bx + vals[y][d]) * SCALE)].append((b, d))

        for key, left in buckets.items():
            right = buckets.get(-key)
            if not right:
                continue

            for b, d in left:
                c = x - b
                e = y - d
                for z, h in right:
                    a = y - h
                    g = x - z
                    quadrilaterals.add(canonical((a, b, c, d, e, z, g, h)))

    return len(quadrilaterals)


if __name__ == "__main__":
    print(solve())
