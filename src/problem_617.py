# Problem 617: https://projecteuler.net/problem=617

from sympy import integer_nthroot


def solve(lim=10**18):
    total = 0
    e = 2
    while 2**e + 2 <= lim:
        k = e
        length = 1
        while 2**k + 2 <= lim:
            m = integer_nthroot(lim, k)[0]
            if m**k + m > lim:
                m -= 1
            total += length * (m - 1)

            r = integer_nthroot(m, e)[0]
            while r > 1:
                total += r - 1
                r = integer_nthroot(r, e)[0]

            k *= e
            length += 1
        e += 1
    return total


if __name__ == "__main__":
    print(solve())
