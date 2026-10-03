# Problem 652: https://projecteuler.net/problem=652

from sympy import integer_nthroot, mobius, totient


def solve(n=10**18):
    roots = [0]
    k = 1
    while 2**k <= n:
        roots.append(int(integer_nthroot(n, k)[0]))
        k += 1

    limit = len(roots) - 1
    mu = [0] + [int(mobius(k)) for k in range(1, limit + 1)]
    total = sum(mu[k] * (roots[k] - 1) ** 2 for k in range(1, limit + 1))

    for t in range(1, limit + 1):
        bases = sum(mu[k] * (roots[t * k] - 1) for k in range(1, limit // t + 1))
        weight = 1 if t == 1 else 2 * int(totient(t))
        total -= weight * (bases - 1)

    return total % 10**9


if __name__ == "__main__":
    print(solve())
