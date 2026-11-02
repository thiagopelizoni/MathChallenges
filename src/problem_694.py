# Problem 694: https://projecteuler.net/problem=694

from sympy import integer_nthroot, primerange


def solve(n=10**18):
    primes = list(primerange(integer_nthroot(n, 3)[0] + 1))

    def visit(d, start):
        total = n // d
        for i in range(start, len(primes)):
            p = primes[i]
            q = d * p**3
            if q > n:
                break
            while q <= n:
                total += visit(q, i + 1)
                q *= p
        return total

    return visit(1, 0)


if __name__ == "__main__":
    print(solve())
