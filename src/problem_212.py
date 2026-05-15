# Problem 212: https://projecteuler.net/problem=212
import numpy as np


def cuboids(n):
    s = [0] * (6 * n + 1)

    for k in range(1, min(55, 6 * n) + 1):
        s[k] = (100003 - 200003 * k + 300007 * k**3) % 1_000_000
    for k in range(56, 6 * n + 1):
        s[k] = (s[k - 24] + s[k - 55]) % 1_000_000

    cubes = []
    for i in range(n):
        j = 6 * i + 1
        x = s[j] % 10000
        y = s[j + 1] % 10000
        z = s[j + 2] % 10000
        dx = 1 + s[j + 3] % 399
        dy = 1 + s[j + 4] % 399
        dz = 1 + s[j + 5] % 399
        cubes.append((x, x + dx, y, y + dy, z, z + dz))

    return cubes


def volume(cubes):
    grid = np.zeros(
        (max(c[3] for c in cubes), max(c[5] for c in cubes)),
        dtype=np.uint16,
    )
    events = []

    for x0, x1, y0, y1, z0, z1 in cubes:
        events.append((x0, 1, y0, y1, z0, z1))
        events.append((x1, -1, y0, y1, z0, z1))

    events.sort()
    area = 0
    total = 0
    prev = events[0][0]

    for x, typ, y0, y1, z0, z1 in events:
        total += area * (x - prev)
        slab = grid[y0:y1, z0:z1]
        if typ == 1:
            area += int(np.count_nonzero(slab == 0))
            slab += 1
        else:
            slab -= 1
            area -= int(np.count_nonzero(slab == 0))
        prev = x

    return total


def solve():
    return volume(cuboids(50_000))


if __name__ == "__main__":
    print(solve())
