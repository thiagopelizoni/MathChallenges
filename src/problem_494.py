# Problem 494: https://projecteuler.net/problem=494

from functools import cache

from sympy import fibonacci


N = 90
SPECIAL = {
    15: (9,),
    16: (19,),
    17: (37,),
    20: (51,),
    50: (159,),
    81: (155,),
}
LAST_SPECIAL = max(SPECIAL)
TAIL_STEPS = N - LAST_SPECIAL
TAIL_MODULUS = 2 * 3**TAIL_STEPS


@cache
def descendant_count(residue, steps):
    if residue % 3 == 0 or steps == 0:
        return 1

    next_modulus = 2 * 3 ** (steps - 1)
    total = descendant_count(2 * residue % next_modulus, steps - 1)
    if residue % 6 == 4:
        total += descendant_count((residue - 1) // 3, steps - 1)
    return total


def solve():
    active = set(SPECIAL[15])
    settled = 0

    for length in range(16, LAST_SPECIAL + 1):
        previous = active
        active = set(SPECIAL.get(length, ()))
        for seed in previous:
            if seed % 6 == 4:
                active.add((seed - 1) // 3)
            if seed % 3:
                active.add(2 * seed)
            else:
                settled += 1

    tail_counts = tuple(
        descendant_count(residue, TAIL_STEPS)
        for residue in range(TAIL_MODULUS)
    )
    excess = settled + sum(
        tail_counts[seed % TAIL_MODULUS] for seed in active
    )
    return int(fibonacci(N)) + excess


if __name__ == "__main__":
    print(solve())
