# Problem 483: https://projecteuler.net/problem=483

from bisect import bisect_right
from math import lcm, prod

import numpy as np
from scipy.signal import fftconvolve


PRIMES = (2, 3, 5, 7, 11, 13, 17)
FFT_LIMIT = 16


def collapse_states(table, exponents):
    grouped = table.copy()
    for axis, exponent in enumerate(exponents):
        if not exponent:
            continue
        lower = [slice(None)] * grouped.ndim
        lower[axis] = slice(0, exponent + 1)
        combined = grouped[tuple(lower)].sum(axis=axis)
        destination = [slice(None)] * grouped.ndim
        destination[axis] = exponent
        grouped[tuple(destination)] = combined
        lower[axis] = slice(0, exponent)
        grouped[tuple(lower)] = 0
    return grouped


def expected_square(n):
    dimensions = []
    for prime in PRIMES:
        dimension = 1
        power = prime
        while power <= n:
            dimension += 1
            power *= prime
        dimensions.append(dimension)
    dimensions = tuple(dimensions)
    state_count = prod(dimensions)

    heads = [0] * (n + 1)
    tails = [None] * (n + 1)
    for length in range(1, n + 1):
        head = length
        exponents = []
        for prime in PRIMES:
            exponent = 0
            while head % prime == 0:
                exponent += 1
                head //= prime
            exponents.append(exponent)
        heads[length] = head
        tails[length] = tuple(exponents)

    table = np.zeros(dimensions + (n + 1,))
    table[(0,) * len(PRIMES) + (0,)] = 1

    for length in range(n, 0, -1):
        if heads[length] != 1:
            continue
        grouped = collapse_states(table, tails[length])
        flat = table.reshape(state_count, n + 1)
        base = grouped.reshape(state_count, n + 1)

        if length <= FFT_LIMIT:
            kernel = np.zeros(n + 1)
            weight = 1.0
            for count in range(1, n // length + 1):
                weight /= length * count
                kernel[count * length] = weight
            flat += fftconvolve(base, kernel[None, :], axes=(-1,))[
                :, : n + 1
            ]
        else:
            weight = 1.0
            for count in range(1, n // length + 1):
                weight /= length * count
                shift = count * length
                flat[:, shift:] += base[:, : n + 1 - shift] * weight

    transformed = table
    for axis, (prime, dimension) in enumerate(zip(PRIMES, dimensions)):
        x = np.arange(dimension)[None, :]
        y = np.arange(dimension)[:, None]
        kernel = np.power(float(prime), 2 * np.maximum(x, y))
        transformed = np.moveaxis(
            np.tensordot(kernel, transformed, axes=(1, axis)),
            0,
            axis,
        )
    transformed = transformed.reshape(state_count, n + 1)

    allowed = tuple(length for length in range(1, n + 1) if heads[length] != 1)
    coordinates = np.indices(dimensions, dtype=np.int16).reshape(
        len(PRIMES), state_count
    ).T
    join_maps = {}
    for tail in {tails[length] for length in allowed}:
        joined = np.maximum(coordinates, np.array(tail, dtype=np.int16))
        join_maps[tail] = np.ravel_multi_index(
            joined.T, dimensions
        ).astype(np.int32)

    cycle_counts = [0] * (n + 1)
    total = 0.0

    def visit(remaining, position, state, period, weight):
        nonlocal total
        total += weight * period * period * transformed[state, remaining]
        position = min(position, bisect_right(allowed, remaining) - 1)
        for index in range(position, -1, -1):
            length = allowed[index]
            cycle_counts[length] += 1
            visit(
                remaining - length,
                index,
                int(join_maps[tails[length]][state]),
                lcm(period, heads[length]),
                weight / (length * cycle_counts[length]),
            )
            cycle_counts[length] -= 1

    visit(n, len(allowed) - 1, 0, 1, 1.0)
    return total


def scientific(value):
    mantissa, exponent = f"{value:.9e}".split("e")
    return f"{mantissa}e{int(exponent)}"


def solve():
    return scientific(expected_square(350))


if __name__ == "__main__":
    print(solve())
