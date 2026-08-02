# Problem 489: https://projecteuler.net/problem=489

from itertools import product

from sympy import factorint
from sympy.ntheory.modular import crt
from sympy.ntheory.residue_ntheory import nthroot_mod


M = 18
N = 1900


def G(a, b):
    resultant = a**3 * (a**6 + 27 * b**2)
    components = []
    for p, exponent in factorint(resultant).items():
        modulus = p**exponent
        while modulus > 1:
            roots = [
                int(root)
                for root in nthroot_mod(-b, 3, modulus, all_roots=True)
                if ((int(root) + a) ** 3 + b) % modulus == 0
            ]
            if roots:
                components.append((modulus, roots))
                break
            modulus //= p

    residues = [0]
    modulus = 1
    for q, roots in components:
        residues = [
            int(crt((modulus, q), (residue, root), check=False)[0])
            for residue, root in product(residues, roots)
        ]
        modulus *= q
    return min(residues)


def solve():
    return sum(G(a, b) for a in range(1, M + 1) for b in range(1, N + 1))


if __name__ == "__main__":
    print(solve())
