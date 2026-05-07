# Problem 184: https://projecteuler.net/problem=184
from collections import Counter
from math import atan2, comb, gcd, pi


def direction_counts(r):
    counts = Counter()
    rr = r * r
    for x in range(1 - r, r):
        for y in range(1 - r, r):
            if x == 0 and y == 0:
                continue
            if x * x + y * y < rr:
                g = gcd(abs(x), abs(y))
                counts[x // g, y // g] += 1
    return counts


def solve():
    counts = direction_counts(105)
    dirs = sorted(counts, key=lambda p: atan2(p[1], p[0]))
    weights = [counts[d] for d in dirs]
    angles = [atan2(y, x) for x, y in dirs]
    n = sum(weights)
    size = len(dirs)

    doubled = weights + weights
    wide_angles = angles + [a + 2 * pi for a in angles]
    pref = [0]
    for w in doubled:
        pref.append(pref[-1] + w)

    bad = 0
    j = 0
    for i in range(size):
        j = max(j, i + 1)
        while j < i + size and wide_angles[j] - wide_angles[i] < pi - 1e-12:
            j += 1
        after = pref[j] - pref[i + 1]
        bad += comb(weights[i] + after, 3) - comb(after, 3)

    seen = set()
    for d, a in counts.items():
        opposite = (-d[0], -d[1])
        if d in seen or opposite not in counts:
            continue
        seen.add(d)
        seen.add(opposite)
        b = counts[opposite]
        bad += a * b * (n - a - b) + comb(a, 2) * b + a * comb(b, 2)

    return comb(n, 3) - bad


if __name__ == "__main__":
    print(solve())
