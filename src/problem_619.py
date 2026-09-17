# Problem 619: https://projecteuler.net/problem=619

from sympy import GF, factorint
from sympy.polys.matrices import DomainMatrix


def count_subsets(a, b, mod):
    field = GF(2)
    rows = {}
    for i, n in enumerate(range(a, b + 1)):
        row = {}
        for p, e in factorint(n).items():
            if e % 2:
                row[b - p] = field.one
        if row:
            rows[i] = row
    m = b - a + 1
    matrix = DomainMatrix.from_dod(rows, (m, b), field)
    _, pivots = matrix.rref(method="GJ")
    return (pow(2, m - len(pivots), mod) - 1) % mod


def solve():
    return count_subsets(1000000, 1234567, 1000000007)


if __name__ == "__main__":
    print(solve())
