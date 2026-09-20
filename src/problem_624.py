# Problem 624: https://projecteuler.net/problem=624

from sympy import GF
from sympy.polys.matrices import DomainMatrix


def solve(n=10**18, p=1_000_000_009):
    field = GF(p)
    half = field(1) / field(2)
    step = DomainMatrix.from_list([[half, half], [half, 0]], field)
    before = step.pow(n - 1)
    series = before * (DomainMatrix.eye(2, field) - step * before).inv()
    q = int(series.to_Matrix()[0, 1]) * int(half) % p
    return q or p


if __name__ == "__main__":
    print(solve())
