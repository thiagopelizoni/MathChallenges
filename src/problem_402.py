# Problem 402: https://projecteuler.net/problem=402

from math import gcd

from sympy import Poly, fibonacci, lucas, symbols
from sympy.polys.domains import GF
from sympy.polys.matrices import DomainMatrix


MOD = 10**9
LAST = 1_234_567_890_123
PERIOD = 24
LUCAS = int(lucas(PERIOD))
X, Y = symbols("x y")
MONOMIALS = (
    (0, 0),
    (1, 0),
    (0, 1),
    (2, 0),
    (1, 1),
    (0, 2),
    (3, 0),
    (2, 1),
    (1, 2),
    (0, 3),
)
DOMAIN = GF(MOD, symmetric=False)


def coefficients():
    result = []
    for r in range(PERIOD):
        a3 = a2 = a1 = a0 = 0
        for a in range(1, PERIOD + 1):
            ea = int(a <= r)
            for b in range(1, PERIOD + 1):
                eb = int(b <= r)
                for c in range(1, PERIOD + 1):
                    ec = int(c <= r)
                    m = gcd(
                        24,
                        a + b + c + 1,
                        2 * (3 * a + b + 7),
                        6 * (a + 6),
                    )
                    a3 += m
                    a2 += m * (ea + eb + ec)
                    a1 += m * (ea * eb + ea * ec + eb * ec)
                    a0 += m * ea * eb * ec
        result.append((a3, a2, a1, a0))
    return result


def transition(r, coeff):
    h = (LUCAS - 2) * r // PERIOD
    nxt = Y, -X + LUCAS * Y + h
    rows = []

    for i, j in MONOMIALS:
        p = Poly(nxt[0] ** i * nxt[1] ** j, X, Y)
        rows.append(
            [int(p.coeff_monomial(X**u * Y**v)) for u, v in MONOMIALS]
            + [0]
        )

    a3, a2, a1, a0 = coeff
    weights = {(0, 0): a0, (1, 0): a1, (2, 0): a2, (3, 0): a3}
    rows.append([weights.get(m, 0) for m in MONOMIALS] + [1])
    return DomainMatrix.from_list(rows, DOMAIN)


def progression_sum(first, count, coeff):
    f = int(fibonacci(first))
    r = f % PERIOD
    x = (f - r) // PERIOD
    y = (int(fibonacci(first + PERIOD)) - r) // PERIOD
    values = [pow(x, i) * pow(y, j) for i, j in MONOMIALS] + [0]
    state = DomainMatrix.from_list([[v] for v in values], DOMAIN)
    return int(((transition(r, coeff) ** count) * state).to_Matrix()[-1, 0])


def solve():
    coeff = coefficients()
    total = 0

    for first in range(2, PERIOD + 2):
        count = (LAST - first) // PERIOD + 1
        r = int(fibonacci(first)) % PERIOD
        total += progression_sum(first, count, coeff[r])

    return total % MOD


if __name__ == "__main__":
    print(solve())
