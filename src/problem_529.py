# Problem 529: https://projecteuler.net/problem=529

import numpy as np


MOD = 1_000_000_007
N = 10**18
BASE = 32_768


def next_state(state, digit):
    digits, uncovered = state
    digits += (digit,)
    uncovered += 1
    total = sum(digits)
    while total > 10:
        if len(digits) == uncovered:
            return None
        total -= digits[0]
        digits = digits[1:]
    if total == 10:
        uncovered = 0
    return digits, uncovered


def build_automaton():
    states = [((), 0)]
    index = {states[0]: 0}
    moves = []
    for state in states:
        row = []
        for digit in range(1, 10):
            nxt = next_state(state, digit)
            if nxt is not None:
                if nxt not in index:
                    index[nxt] = len(states)
                    states.append(nxt)
                row.append(index[nxt])
        moves.append(row)
    accepting = [i for i, (digits, uncovered) in enumerate(states) if digits and uncovered == 0]
    return moves, accepting


def sequence(moves, accepting, count):
    dp = [0] * len(moves)
    dp[0] = 1
    values = [0]
    for _ in range(1, count):
        nxt = [0] * len(moves)
        for i, value in enumerate(dp):
            if value:
                for j in moves[i]:
                    nxt[j] += value
                    if nxt[j] >= MOD:
                        nxt[j] -= MOD
        dp = nxt
        values.append(sum(dp[i] for i in accepting) % MOD)
    return values


def berlekamp_massey(values):
    c = [1]
    old = [1]
    length = 0
    shift = 1
    last = 1
    for n in range(len(values)):
        delta = values[n]
        for i in range(1, length + 1):
            delta = (delta + c[i] * values[n - i]) % MOD
        if delta == 0:
            shift += 1
            continue
        factor = delta * pow(last, MOD - 2, MOD) % MOD
        previous = c[:]
        needed = max(length + shift, len(old) - 1 + shift)
        c.extend([0] * (needed + 1 - len(c)))
        for i, value in enumerate(old):
            c[i + shift] = (c[i + shift] - factor * value) % MOD
        if 2 * length <= n:
            length = n + 1 - length
            old = previous
            last = delta
            shift = 1
        else:
            shift += 1
    return [(-c[i]) % MOD for i in range(1, length + 1)]


def convolve(a, b):
    a = np.asarray(a, dtype=np.int64)
    b = np.asarray(b, dtype=np.int64)
    low_a, high_a = a % BASE, a // BASE
    low_b, high_b = b % BASE, b // BASE
    low = np.convolve(low_a, low_b)
    middle = np.convolve(low_a, high_b) + np.convolve(high_a, low_b)
    high = np.convolve(high_a, high_b)
    return (low % MOD + (middle % MOD) * BASE + (high % MOD) * (BASE * BASE % MOD)) % MOD


def invert_series(f, size):
    inverse = np.array([pow(int(f[0]), MOD - 2, MOD)], dtype=np.int64)
    while len(inverse) < size:
        length = min(2 * len(inverse), size)
        correction = (-convolve(f[:length], inverse)[:length]) % MOD
        correction[0] = (correction[0] + 2) % MOD
        inverse = convolve(inverse, correction)[:length]
    return inverse


def power_coefficients(recurrence, exponent):
    degree = len(recurrence)
    polynomial = np.zeros(degree + 1, dtype=np.int64)
    polynomial[-1] = 1
    for i, value in enumerate(recurrence):
        polynomial[degree - 1 - i] = -value % MOD
    inverse = invert_series(polynomial[::-1], degree - 1)

    def multiply(a, b):
        product = convolve(a, b)
        quotient = convolve(product[::-1][: degree - 1], inverse)[: degree - 1][::-1]
        return (product[:degree] - convolve(quotient, polynomial)[:degree]) % MOD

    result = np.zeros(degree, dtype=np.int64)
    result[0] = 1
    base = np.zeros(degree, dtype=np.int64)
    base[:2] = 1
    while exponent:
        if exponent % 2:
            result = multiply(result, base)
        exponent //= 2
        if exponent:
            base = multiply(base, base)
    return result


def solve():
    moves, accepting = build_automaton()
    values = sequence(moves, accepting, 2 * len(moves) + 5)
    recurrence = berlekamp_massey(values)
    coefficients = power_coefficients(recurrence, N)
    return sum(int(coefficients[i]) * values[i] for i in range(len(recurrence))) % MOD


if __name__ == "__main__":
    print(solve())
