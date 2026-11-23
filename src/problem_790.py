# Problem 790: https://projecteuler.net/problem=790

from itertools import pairwise
from operator import add, mul


def solve(steps=10**5):
    side = 50515093
    s = 290797
    events = []
    edges = {0, side}
    for _ in range(steps):
        coords = []
        for _ in range(4):
            coords.append(s)
            s = s * s % side
        x1, x2 = sorted(coords[:2])
        y1, y2 = sorted(coords[2:])
        stop = y2 + 1
        edges.update((y1, stop))
        events.append((x1, y1, stop, 1))
        events.append((x2 + 1, y1, stop, -1))

    ys = sorted(edges)
    index = {y: i for i, y in enumerate(ys)}
    size = 1
    while size < len(ys) - 1:
        size *= 2
    counts = [[0] * 12 for _ in range(2 * size)]
    turns = [0] * (2 * size)
    for i, (lo, hi) in enumerate(pairwise(ys), size):
        counts[i][0] = hi - lo
    for i in range(size - 1, 0, -1):
        counts[i][0] = counts[2 * i][0] + counts[2 * i + 1][0]

    def update(node, left, right, lo, hi, step):
        if lo <= left and right <= hi:
            turns[node] = (turns[node] + step) % 12
            row = counts[node]
            shift = step
        else:
            mid = (left + right) // 2
            if lo < mid:
                update(2 * node, left, mid, lo, hi, step)
            if mid < hi:
                update(2 * node + 1, mid, right, lo, hi, step)
            row = list(map(add, counts[2 * node], counts[2 * node + 1]))
            shift = turns[node]
        counts[node] = row[-shift:] + row[:-shift] if shift else row

    hours = (12, *range(1, 12))
    total = 0
    prev = 0
    events.sort()
    for x, y1, stop, step in events:
        if x != prev:
            total += (x - prev) * sum(map(mul, hours, counts[1]))
            prev = x
        update(1, 0, size, index[y1], index[stop], step)
    return total + (side - prev) * side * 12


if __name__ == "__main__":
    print(solve())
