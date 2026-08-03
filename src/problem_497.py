# Problem 497: https://projecteuler.net/problem=497

from itertools import permutations


MOD = 10**9
STATES = tuple(permutations(range(3)))
STATE_INDEX = {state: i for i, state in enumerate(STATES)}
EDGES = tuple(permutations(range(3), 2))
EDGE_INDEX = {edge: i for i, edge in enumerate(EDGES)}
TRANSITIONS = tuple(
    (STATE_INDEX[s, u, t], STATE_INDEX[u, t, s]) for s, t, u in STATES
)
CYCLES = tuple(
    tuple(int(edge in ((u, s), (s, t), (t, u))) for edge in EDGES)
    for s, t, u in STATES
)
INITIAL = tuple(
    tuple(int(edge == (s, t)) for edge in EDGES) for s, t, _ in STATES
)


def advance(coefficients):
    return tuple(
        tuple(
            (
                coefficients[left][j]
                + coefficients[right][j]
                + CYCLES[i][j]
            )
            % MOD
            for j in range(6)
        )
        for i, (left, right) in enumerate(TRANSITIONS)
    )


def travel_costs(k, positions):
    costs = []
    for x, y in EDGES:
        start, end = positions[x], positions[y]
        if x < y:
            cost = (end - start) * (start + end - 2)
        else:
            cost = (start - end) * (2 * k - start - end)
        costs.append(cost % MOD)
    return costs


def solve():
    coefficients = INITIAL
    k = 1
    positions = (1, 1, 1)
    total = 0
    target = STATE_INDEX[0, 2, 1]
    start = EDGE_INDEX[1, 0]

    for n in range(1, 10_001):
        if n > 1:
            coefficients = advance(coefficients)
        k = 10 * k % MOD
        positions = tuple(
            base * position % MOD
            for base, position in zip((3, 6, 9), positions)
        )
        costs = travel_costs(k, positions)
        total += costs[start] + sum(
            coefficient * cost
            for coefficient, cost in zip(coefficients[target], costs)
        )
        total %= MOD
    return total


if __name__ == "__main__":
    print(solve())
