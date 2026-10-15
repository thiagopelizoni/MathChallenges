# Problem 670: https://projecteuler.net/problem=670
from sympy import GF
from sympy.polys.matrices import DomainMatrix


def F(n, mod):
    states = ["V"]
    for a in range(3):
        for b in range(3):
            states.append((a, b))
    idx = {s: i for i, s in enumerate(states)}
    k = len(states)

    M = [[0] * k for _ in range(k)]
    v = idx["V"]
    M[v][v] = 3
    for a in range(3):
        for b in range(3):
            M[v][idx[a, b]] += 6
    for a in range(3):
        for b in range(3):
            i = idx[a, b]
            if a > 0 and b > 0:
                M[i][idx[a - 1, b - 1]] += 1
            elif a == 0 and b > 0:
                for l in range(3):
                    M[i][idx[l, b - 1]] += 2
            elif a > 0 and b == 0:
                for l in range(3):
                    M[i][idx[a - 1, l]] += 2
            else:
                M[i][v] += 2

    start = [0] * k
    start[v] = 4
    for a in range(3):
        for b in range(3):
            start[idx[a, b]] = 12

    T = DomainMatrix(M, (k, k), GF(mod)).pow(n - 1)
    row = DomainMatrix([start], (1, k), GF(mod)) * T
    res = row.to_Matrix()
    return int(res[0, v] + res[0, idx[0, 0]]) % mod


def solve():
    return F(10**16, 1000004321)


if __name__ == "__main__":
    print(solve())
