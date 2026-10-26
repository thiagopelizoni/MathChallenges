# Problem 686: https://projecteuler.net/problem=686
from decimal import Decimal, getcontext


def solve(L=123, n=678910):
    getcontext().prec = 60
    M = 10**40
    s = 10 ** (len(str(L)) - 1)
    a = int(Decimal(2).log10() * M)
    lo = int((Decimal(L) / s).log10() * M)
    hi = int((Decimal(L + 1) / s).log10() * M)
    w = hi - lo

    def hit(j):
        return lo <= j * a % M < hi

    j = 1
    while not hit(j):
        j += 1

    steps = []
    d = 0
    for _ in range(n - 1):
        k = 0
        while True:
            if k == len(steps):
                d += 1
                while w <= d * a % M <= M - w:
                    d += 1
                steps.append(d)
            if hit(j + steps[k]):
                j += steps[k]
                break
            k += 1
    return j


if __name__ == "__main__":
    print(solve())
