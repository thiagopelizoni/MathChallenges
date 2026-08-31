# Problem 576: https://projecteuler.net/problem=576
from math import ceil

import numpy as np
from sympy import primerange


def next_free(parent, i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i


def jump_events(p, gap):
    one = np.longdouble(1)
    step = one / np.sqrt(np.longdouble(p))
    domain = one - gap
    count = ceil(domain / gap)

    while True:
        jumps = np.arange(1, count + 1, dtype=np.longdouble)
        positions = np.remainder(jumps * step, one)
        ordered = np.sort(positions)
        if ordered[0] <= gap and ordered[-1] >= domain and np.max(np.diff(ordered)) <= gap:
            break
        count *= 2

    left = np.maximum(positions - gap, 0)
    right = np.minimum(positions, domain)
    ends = np.array([0, domain], dtype=np.longdouble)
    bounds = np.unique(np.concatenate((ends, left, right)))
    starts = np.searchsorted(bounds, left)
    stops = np.searchsorted(bounds, right)
    times = np.empty(len(bounds) - 1, dtype=int)
    parent = np.arange(len(bounds), dtype=int)
    remaining = len(times)

    for jump, (start, stop) in enumerate(zip(starts, stops), 1):
        i = next_free(parent, int(start))
        while i < stop:
            times[i] = jump
            parent[i] = next_free(parent, i + 1)
            remaining -= 1
            i = int(parent[i])
        if remaining == 0:
            break

    changes = np.flatnonzero(times[1:] != times[:-1]) + 1
    deltas = (times[changes] - times[changes - 1]) * step
    return times[0] * step, bounds[changes], deltas


def solve():
    limit = 100
    gap = np.longdouble("0.00002")
    initial = np.longdouble(0)
    events = []

    for p in primerange(2, limit + 1):
        value, coordinates, deltas = jump_events(p, gap)
        initial += value
        events.append((coordinates, deltas))

    coordinates = np.concatenate([event[0] for event in events])
    deltas = np.concatenate([event[1] for event in events])
    events.clear()
    order = np.argsort(coordinates)
    changes = np.cumsum(deltas[order], dtype=np.longdouble)
    best = initial + max(np.longdouble(0), np.max(changes))
    return f"{best:.4f}"


if __name__ == "__main__":
    print(solve())
