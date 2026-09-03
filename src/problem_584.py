# Problem 584: https://projecteuler.net/problem=584

from itertools import product

import numpy as np


def solve():
    days = 365
    group = 4
    radius = 7
    places = 8
    cap = radius + 1
    width = group - 2
    states = list(product(range(cap + 1), repeat=width))
    index = {state: i for i, state in enumerate(states)}
    transitions = []
    tails = []

    for source, state in enumerate(states):
        zeros = 0
        for value in reversed(state):
            if value != 0:
                break
            zeros += 1
        for gap in range(cap + 1):
            if sum(state) + gap < cap:
                continue
            target = index[state[1:] + (gap,)]
            if gap == cap:
                tails.append((source, target))
            else:
                weight = np.longdouble(1) / (zeros + 2) if gap == 0 else np.longdouble(1)
                transitions.append((source, target, gap, weight))

    count = len(states)
    paths = np.zeros((count, count, days + 1), dtype=np.longdouble)
    paths[np.arange(count), np.arange(count), 0] = 1
    expected = np.longdouble(group)
    fact = 1
    power = 1
    max_people = (group - 1) * days // cap

    for n in range(1, max_people + 1):
        new = np.zeros_like(paths)
        for source, target, gap, weight in transitions:
            new[:, target, gap:] += weight * paths[:, source, :days + 1 - gap]
        for source, target in tails:
            sums = np.cumsum(paths[:, source, :days + 1 - cap], axis=1)
            new[:, target, cap:] += sums
        paths = new
        fact *= n
        power *= days
        if n >= group:
            cycles = paths[np.arange(count), np.arange(count), days].sum()
            expected += np.longdouble(fact // n) * cycles / np.longdouble(power // days)

    return f"{expected:.{places}f}"


if __name__ == "__main__":
    print(solve())
