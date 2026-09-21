# Problem 626: https://projecteuler.net/problem=626

from math import factorial, gcd

from sympy import multiplicity
from sympy.utilities.iterables import partitions


def solve(n=20):
    mod = 1_001_001_011
    valuations = [0] + [int(multiplicity(2, k)) for k in range(1, n + 1)]
    types = []
    for partition in partitions(n):
        cycles = list(partition.items())
        z = 1
        for length, count in cycles:
            z *= length**count * factorial(count)
        count = sum(partition.values())
        least = min(valuations[length] for length in partition)
        types.append((cycles, count, least, pow(z, -1, mod)))

    total = 0
    for i, (rows, r, row_min, row_weight) in enumerate(types):
        for j in range(i + 1):
            columns, c, column_min, column_weight = types[j]
            orbits = sum(gcd(a, b) * x * y for a, x in rows for b, y in columns)
            if row_min == column_min:
                free = 1
            elif row_min < column_min:
                free = sum(x for a, x in rows if valuations[a] < column_min)
            else:
                free = sum(y for b, y in columns if valuations[b] < row_min)
            fixed = pow(2, orbits - r - c + free, mod)
            weight = row_weight * column_weight
            total += (1 if i == j else 2) * fixed * weight
    return total % mod


if __name__ == "__main__":
    print(solve())
