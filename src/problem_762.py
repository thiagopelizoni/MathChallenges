# Problem 762: https://projecteuler.net/problem=762

from collections import defaultdict, deque
from functools import cache


def solve(n=100_000):
    height = 4
    mod = 10**9
    children = [frozenset((y, (y + 1) % height)) for y in range(height)]

    @cache
    def column(incoming):
        endings = defaultdict(set)

        def visit(i, cells, outgoing):
            if i == len(incoming):
                endings[cells].add(outgoing)
            elif cells.isdisjoint(children[incoming[i]]):
                visit(i + 1, cells.union(children[incoming[i]]), outgoing)

            if len(outgoing) < height - 1:
                for y in cells:
                    visit(i, cells.difference((y,)), outgoing + (y,))

        visit(0, frozenset(), ())
        return endings

    finished = frozenset({()})
    start = frozenset({(0,)})
    states = [finished, start]
    transitions = []
    for state in states:
        if state == finished:
            continue
        by_cells = defaultdict(set)
        for incoming in state:
            for cells, orders in column(incoming).items():
                by_cells[cells].update(orders)

        destinations = []
        for orders in by_cells.values():
            dest = frozenset(orders)
            if dest not in states:
                states.append(dest)
            destinations.append(states.index(dest))
        divisions = len(next(iter(state)))
        transitions.append((divisions, destinations))

    if n == 0:
        return 1
    ways = deque(([0] * len(states) for _ in range(height - 1)), maxlen=height - 1)
    ways[-1][0] = 1
    for _ in range(n):
        counts = [0]
        for divisions, destinations in transitions:
            previous = ways[-divisions]
            counts.append(sum(previous[j] for j in destinations) % mod)
        ways.append(counts)
    return ways[-1][1]


if __name__ == "__main__":
    print(f"{solve():09d}")
