# Problem 368: https://projecteuler.net/problem=368

from math import comb, fsum

import numpy as np


CUTOFF_LEN = 5
TAIL_DEGREE = 5
DIGITS = range(10)
STATES = [(d, run) for d in DIGITS for run in (1, 2)]
INDEX = {state: i for i, state in enumerate(STATES)}


def next_state(state, d):
    last, run = state
    if d == last:
        if run == 2:
            return None
        return d, 2
    return d, 1


def tail_constants(degree):
    constants = []
    size = len(STATES)

    for j in range(degree + 1):
        scale = 10.0 ** -(j + 1)
        mat = np.eye(size)
        rhs = np.zeros(size)

        for i, state in enumerate(STATES):
            for d in DIGITS:
                nxt = next_state(state, d)
                if nxt is None:
                    continue

                mat[i, INDEX[nxt]] -= scale
                val = d**j
                for m, prev in enumerate(constants):
                    val += comb(j, m) * d ** (j - m) * prev[INDEX[nxt]]
                rhs[i] += scale * val

        constants.append(np.linalg.solve(mat, rhs))

    return constants


def next_prefixes(prefixes):
    out = []
    for p, state in prefixes:
        for d in DIGITS:
            nxt = next_state(state, d)
            if nxt is not None:
                out.append((10 * p + d, nxt))
    return out


def series_value():
    constants = tail_constants(TAIL_DEGREE)
    prefixes = [(d, (d, 1)) for d in range(1, 10)]
    terms = []

    for _ in range(1, CUTOFF_LEN):
        terms.extend(1.0 / p for p, _ in prefixes)
        prefixes = next_prefixes(prefixes)

    for p, state in prefixes:
        inv = 1.0 / p
        power = inv
        sign = 1.0
        total = inv
        i = INDEX[state]

        for constant in constants:
            total += sign * constant[i] * power
            power *= inv
            sign = -sign

        terms.append(total)

    return fsum(terms)


def solve():
    return f"{series_value():.10f}"


if __name__ == "__main__":
    print(solve())
