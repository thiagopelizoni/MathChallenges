# Problem 644: https://projecteuler.net/problem=644

from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
from math import sqrt
from operator import xor

from scipy.optimize import brentq


root = sqrt(2)
pieces = (((1, 0), 1.0), ((0, 1), root))


def length(pair):
    return pair[0] + pair[1] * root


def grundy_runs(limit):
    events = {}
    heap = []
    counts = defaultdict(int)

    def schedule(pair, g, change):
        x = length(pair)
        if x > limit:
            return
        if pair not in events:
            events[pair] = defaultdict(int)
            heappush(heap, (x, pair))
        events[pair][g] += change

    for piece, _ in pieces:
        schedule(piece, 0, 1)

    starts = [(0, 0)]
    ends = []
    values = [0]

    while heap:
        x, point = heappop(heap)
        for g, change in events.pop(point).items():
            counts[g] += change

        new_value = 0
        while counts[new_value] > 0:
            new_value += 1
        if new_value == values[-1]:
            continue

        for end, g in zip(ends, values[:-1]):
            for piece, _ in pieces:
                event = (
                    point[0] + end[0] + piece[0],
                    point[1] + end[1] + piece[1],
                )
                schedule(event, xor(values[-1], g), -1)
        for piece, _ in pieces:
            event = (2 * point[0] + piece[0], 2 * point[1] + piece[1])
            schedule(event, 0, -1)

        ends.append(point)
        starts.append(point)
        values.append(new_value)

        for start, g in zip(starts[:-1], values[:-1]):
            for piece, _ in pieces:
                event = (
                    point[0] + start[0] + piece[0],
                    point[1] + start[1] + piece[1],
                )
                schedule(event, xor(new_value, g), 1)
        for piece, _ in pieces:
            event = (2 * point[0] + piece[0], 2 * point[1] + piece[1])
            schedule(event, 0, 1)

    ends.append((limit, 0))
    return starts, ends, values


def winning_events(starts, ends, values, limit):
    runs = defaultdict(list)
    for start, end, g in zip(starts, ends, values):
        runs[g].append((start, end))

    changes = defaultdict(int)
    for intervals in runs.values():
        for i, (a, b) in enumerate(intervals):
            for j in range(i, len(intervals)):
                c, d = intervals[j]
                factor = 1 if i == j else 2
                ac = (a[0] + c[0], a[1] + c[1])
                ad = (a[0] + d[0], a[1] + d[1])
                bc = (b[0] + c[0], b[1] + c[1])
                bd = (b[0] + d[0], b[1] + d[1])
                if length(ac) <= limit:
                    changes[ac] += factor
                if length(ad) <= limit:
                    changes[ad] -= factor
                if length(bc) <= limit:
                    changes[bc] -= factor
                if length(bd) <= limit:
                    changes[bd] += factor

    slope = 0
    total = 0.0
    previous = 0.0
    data = []
    for point in sorted(changes, key=length):
        x = length(point)
        total += slope * (x - previous)
        slope += changes[point]
        data.append((x, total, slope, point))
        previous = x
    return data


def solve(low=200, high=500):
    starts, ends, values = grundy_runs(high)
    data = winning_events(starts, ends, values, high)
    event_points = [row[0] for row in data]

    def line(s):
        i = bisect_right(event_points, s) - 1
        x, total, slope, _ = data[i]
        return slope, total - slope * x

    def winning_measure(s):
        slope, intercept = line(s)
        return slope * s + intercept

    def gain(x):
        straight = winning_measure(x - 1) / (x - 1)
        diagonal = winning_measure(x - root) / (x - root)
        return x * (straight + diagonal) / 2

    cuts = {(low, 0), (high, 0)}
    for _, _, _, point in data:
        for piece, _ in pieces:
            cut = (point[0] + piece[0], point[1] + piece[1])
            if low <= length(cut) <= high:
                cuts.add(cut)
    cuts = sorted(cuts, key=length)

    best = max(gain(length(point)) for point in cuts)
    for left, right in zip(cuts, cuts[1:]):
        a = length(left)
        b = length(right)
        middle = (a + b) / 2
        m1, c1 = line(middle - 1)
        m2, c2 = line(middle - root)
        total_slope = m1 + m2

        def derivative(x):
            return total_slope - c1 / (x - 1) ** 2 - c2 * root / (x - root) ** 2

        parts = [a, b]
        first = c1
        second = c2 * root
        if first * second < 0:
            ratio = (-second / first) ** (1 / 3)
            if ratio != 1:
                turning = (root - ratio) / (1 - ratio)
                if a < turning < b:
                    parts.insert(1, turning)

        for start, end in zip(parts, parts[1:]):
            if derivative(start) > 0 and derivative(end) < 0:
                point = brentq(derivative, start, end)
                best = max(best, gain(point))

    return f"{best:.8f}"


if __name__ == "__main__":
    print(solve())
