# Problem 416: https://projecteuler.net/problem=416

from math import comb

import numpy as np
from scipy.sparse import csr_array
from sympy import GF
from sympy.polys.matrices import DomainMatrix


MOD = 10**9
PATHS = 20
SQUARES = 10**12


def operators(p):
    states = [
        (a, b, p - a - b)
        for a in range(p + 1)
        for b in range(p - a + 1)
    ]
    index = {state: i for i, state in enumerate(states)}
    size = len(states)
    rows = [[0] * size for _ in range(size)]
    b_rows = []
    b_cols = []

    for row, (a, b, c) in enumerate(states):
        for i in range(a + 1):
            for j in range(a - i + 1):
                k = a - i - j
                col = index[i + b, j + c, k]
                rows[row][col] += comb(a, i) * comb(a - i, j)
        if a == 0:
            col = index[b, c, 0]
            rows[row][col] -= 1
            b_rows.append(row)
            b_cols.append(col)

    t_rows = []
    t_cols = []
    values = []
    for row, entries in enumerate(rows):
        for col, value in enumerate(entries):
            if value:
                t_rows.append(row)
                t_cols.append(col)
                values.append(value)

    shape = (size, size)
    transition = csr_array(
        (np.array(values, dtype=np.int64), (t_rows, t_cols)), shape=shape
    )
    forbidden = csr_array(
        (np.ones(len(b_rows), dtype=np.int64), (b_rows, b_cols)), shape=shape
    )
    finish = np.zeros(size, dtype=np.int64)
    for i in range(p + 1):
        for j in range(p - i + 1):
            k = p - i - j
            finish[index[i, j, k]] = comb(p, i) * comb(p - i, j)
    start = np.zeros(size, dtype=np.int64)
    start[index[p, 0, 0]] = 1
    return rows, transition, forbidden, finish, start


def initial_terms(transition, forbidden, finish, start, count):
    values = start
    derivative = np.zeros(start.size, dtype=np.int64)
    terms = []

    for _ in range(count):
        terms.append(int(finish.dot((values + derivative) % MOD) % MOD))
        previous = values
        values = transition.dot(values) % MOD
        derivative = (transition.dot(derivative) + forbidden.dot(previous)) % MOD

    return terms


def recurrence(rows):
    domain = GF(MOD)
    characteristic = [
        int(value) % MOD
        for value in DomainMatrix.from_list(rows, domain).charpoly()
    ]
    zeros = 0
    for value in reversed(characteristic):
        if value:
            break
        zeros += 1
    reduced = characteristic[:-zeros]
    squared = [0] * (2 * len(reduced) - 1)
    for i, a in enumerate(reduced):
        for j, b in enumerate(reduced):
            squared[i + j] = (squared[i + j] + a * b) % MOD
    return 2 * zeros, squared


def multiply(a, b, recurrence):
    degree = len(recurrence) - 1
    product = [0] * (2 * degree - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    product[i + j] = (product[i + j] + x * y) % MOD

    for k in range(2 * degree - 2, degree - 1, -1):
        value = product[k]
        if value:
            for j in range(1, degree + 1):
                product[k - j] = (
                    product[k - j] - value * recurrence[j]
                ) % MOD
    return product[:degree]


def linear_term(initial, n, recurrence):
    degree = len(recurrence) - 1
    result = [1] + [0] * (degree - 1)
    power = [0, 1] + [0] * (degree - 2)

    while n:
        n, remainder = divmod(n, 2)
        if remainder:
            result = multiply(result, power, recurrence)
        if n:
            power = multiply(power, power, recurrence)

    return sum(a * b for a, b in zip(result, initial)) % MOD


def frog_paths(p, n):
    rows, transition, forbidden, finish, start = operators(p)
    exponent = n - 2
    if exponent < 2 * len(rows):
        return initial_terms(
            transition, forbidden, finish, start, exponent + 1
        )[exponent]
    shift, rec = recurrence(rows)
    degree = len(rec) - 1
    terms = initial_terms(transition, forbidden, finish, start, shift + degree)
    return linear_term(terms[shift:], exponent - shift, rec)


def solve():
    return frog_paths(PATHS, SQUARES)


if __name__ == "__main__":
    print(solve())
