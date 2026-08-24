# Problem 562: https://projecteuler.net/problem=562
from math import gcd, isqrt, sqrt

import numpy as np
from scipy.spatial import cKDTree


def shell_points(r, width):
    rr = r * r
    points = []
    for x in range(r + 1):
        rest = rr - x * x
        high = isqrt(rest)
        low_square = rest - width
        low = 0 if low_square <= 0 else isqrt(low_square - 1) + 1
        for y in range(low, high + 1):
            points.append((x, y))
            if x:
                points.append((-x, y))
            if y:
                points.append((x, -y))
                if x:
                    points.append((-x, -y))
    return np.array(points, dtype=np.int64)


def solve():
    r = 10 ** 7
    rr = r * r

    a = isqrt(rr // 2)
    best = 0
    while True:
        b = isqrt(rr - (a + 1) * (a + 1))
        x = 2 * a + 1
        y = 2 * b + 1
        length = x * x + y * y
        if b <= a and gcd(x, y) == 1 and length > best:
            best = length
        if b <= a and best and 4 * (a - b) + 2 >= 4 * rr - best:
            break
        a += 1

    bound = 4 * rr - best
    points = shell_points(r, (bound - 1) // 2)
    pairs = cKDTree(points).query_pairs(sqrt(bound), output_type="ndarray")
    edges = points[pairs[:, 0]] + points[pairs[:, 1]]
    lengths = np.sum(edges * edges, axis=1)
    primitive = np.gcd(np.abs(edges[:, 0]), np.abs(edges[:, 1])) == 1
    lengths = np.where(primitive, lengths, 0)

    x, y = map(int, edges[int(np.argmax(lengths))])
    length = x * x + y * y
    s = y * pow(x, -1, length) % length
    numerator = (s * s + 1) * ((length - s) * (length - s) + 1)
    denominator = 4 * length * rr

    answer = isqrt(numerator // denominator)
    if 4 * numerator >= denominator * (2 * answer + 1) ** 2:
        answer += 1
    return answer


if __name__ == "__main__":
    print(solve())
