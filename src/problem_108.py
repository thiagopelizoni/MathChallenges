# Problem 108: https://projecteuler.net/problem=108

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
TARGET = 1999


def solve():
    best = 1
    for p in PRIMES:
        best *= p

    def search(i, last, n, divs):
        nonlocal best
        if divs > TARGET:
            best = min(best, n)
            return
        if i == len(PRIMES):
            return

        p = PRIMES[i]
        m = n
        for e in range(1, last + 1):
            m *= p
            if m >= best:
                break
            search(i + 1, e, m, divs * (2 * e + 1))

    search(0, 10, 1, 1)
    return best


if __name__ == "__main__":
    print(solve())
