# Problem 502: https://projecteuler.net/problem=502

import numpy as np


MOD = 1_000_000_007
INV2 = (MOD + 1) // 2
TASKS = ((10**12, 100), (10_000, 10_000), (100, 10**12))


def step(even, odd, alternating):
    even_suffix = np.cumsum(even[::-1], dtype=np.int64)[::-1] % MOD
    odd_suffix = np.cumsum(odd[::-1], dtype=np.int64)[::-1] % MOD
    total = np.cumsum((even + odd) % MOD, dtype=np.int64) % MOD
    difference = (even - odd) % MOD
    alternating_sum = np.cumsum(
        difference * alternating % MOD, dtype=np.int64
    ) % MOD
    signed = alternating_sum * alternating % MOD
    even_prefix = (total + signed) % MOD * INV2 % MOD
    odd_prefix = (total - signed) % MOD * INV2 % MOD

    next_even = np.empty_like(even)
    next_odd = np.empty_like(odd)
    next_even[:-1] = (even_suffix[1:] + even_prefix[:-1]) % MOD
    next_odd[:-1] = (odd_suffix[1:] + odd_prefix[:-1]) % MOD
    next_even[-1] = even_prefix[-1]
    next_odd[-1] = odd_prefix[-1]
    next_even[0] = 0
    next_odd[0] = 0
    return next_even, next_odd


def bounded_castles(width, height):
    if height <= 0:
        return 0
    even = np.zeros(height + 1, dtype=np.int64)
    odd = np.zeros(height + 1, dtype=np.int64)
    even[0] = 1
    alternating = np.ones(height + 1, dtype=np.int64)
    alternating[1::2] = MOD - 1
    for _ in range(width):
        even, odd = step(even, odd, alternating)
    return int(even[1:].sum() % MOD)


def castles_dp(width, height):
    return (
        bounded_castles(width, height)
        - bounded_castles(width, height - 1)
    ) % MOD


def berlekamp_massey(sequence):
    current = [1]
    previous = [1]
    length = 0
    shift = 1
    scale = 1
    for n, value in enumerate(sequence):
        discrepancy = value
        for i in range(1, length + 1):
            discrepancy += current[i] * sequence[n - i]
        discrepancy %= MOD
        if discrepancy == 0:
            shift += 1
            continue

        factor = discrepancy * pow(scale, MOD - 2, MOD) % MOD
        saved = current[:]
        if len(current) < len(previous) + shift:
            current += [0] * (len(previous) + shift - len(current))
        for i, coefficient in enumerate(previous):
            current[i + shift] -= factor * coefficient
            current[i + shift] %= MOD
        if 2 * length <= n:
            length = n + 1 - length
            previous = saved
            scale = discrepancy
            shift = 1
        else:
            shift += 1
    return [(-current[i]) % MOD for i in range(1, length + 1)]


def combine(a, b, recurrence):
    size = len(recurrence)
    product = [0] * (2 * size)
    for i, left in enumerate(a):
        if left:
            for j, right in enumerate(b):
                if right:
                    product[i + j] += left * right
                    product[i + j] %= MOD
    for i in range(2 * size - 2, size - 1, -1):
        value = product[i]
        if value:
            for j, coefficient in enumerate(recurrence, 1):
                product[i - j] += value * coefficient
                product[i - j] %= MOD
    return product[:size]


def linear_term(initial, recurrence, n):
    size = len(recurrence)
    if n < len(initial):
        return initial[n]
    if size == 0:
        return 0
    result = [1] + [0] * (size - 1)
    power = [0] * size
    if size == 1:
        power[0] = recurrence[0]
    else:
        power[1] = 1
    while n:
        if n % 2:
            result = combine(result, power, recurrence)
        power = combine(power, power, recurrence)
        n //= 2
    return sum(a * b for a, b in zip(result, initial)) % MOD


def bounded_large_width(width, height):
    if height <= 0:
        return 0
    even = np.zeros(height + 1, dtype=np.int64)
    odd = np.zeros(height + 1, dtype=np.int64)
    even[0] = 1
    alternating = np.ones(height + 1, dtype=np.int64)
    alternating[1::2] = MOD - 1
    sequence = [0]
    for _ in range(1, 8 * (height + 1) + 20):
        even, odd = step(even, odd, alternating)
        sequence.append(int(even[1:].sum() % MOD))
    recurrence = berlekamp_massey(sequence)
    return linear_term(sequence[: len(recurrence)], recurrence, width)


def lagrange_consecutive(values, x):
    degree = len(values) - 1
    if 0 <= x <= degree:
        return values[x]
    factorial = [1] * (degree + 1)
    for i in range(1, degree + 1):
        factorial[i] = factorial[i - 1] * i % MOD
    inverse = [1] * (degree + 1)
    inverse[degree] = pow(factorial[degree], MOD - 2, MOD)
    for i in range(degree, 0, -1):
        inverse[i - 1] = inverse[i] * i % MOD

    prefix = [1] * (degree + 2)
    suffix = [1] * (degree + 2)
    for i in range(degree + 1):
        prefix[i + 1] = prefix[i] * (x - i) % MOD
    for i in range(degree, -1, -1):
        suffix[i] = suffix[i + 1] * (x - i) % MOD

    result = 0
    for i, value in enumerate(values):
        coefficient = inverse[i] * inverse[degree - i] % MOD
        if (degree - i) % 2:
            coefficient = -coefficient
        result += value * prefix[i] % MOD * suffix[i + 1] % MOD * coefficient
        result %= MOD
    return result


def large_height_castles(width, height):
    values = [0] + [
        castles_dp(width, h) for h in range(1, 2 * width + 3)
    ]
    if height % 2:
        samples = [values[2 * x + 1] for x in range(width + 1)]
        return lagrange_consecutive(samples, (height - 1) // 2)
    samples = [values[2 * x + 2] for x in range(width + 1)]
    return lagrange_consecutive(samples, (height - 2) // 2)


def castles(width, height):
    if height <= 220:
        return (
            bounded_large_width(width, height)
            - bounded_large_width(width, height - 1)
        ) % MOD
    if width <= 220:
        return large_height_castles(width, height)
    return castles_dp(width, height)


def solve():
    return sum(castles(width, height) for width, height in TASKS) % MOD


if __name__ == "__main__":
    print(solve())
