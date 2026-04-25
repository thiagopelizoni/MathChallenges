# Problem 119: https://projecteuler.net/problem=119


def digit_sum(n):
    return sum(map(int, str(n)))


def candidates(lim):
    vals = set()
    for s in range(2, 9 * len(str(lim)) + 1):
        n = s * s
        while n < lim:
            if n >= 10 and digit_sum(n) == s:
                vals.add(n)
            n *= s
    return sorted(vals)


def solve():
    lim = 100
    while True:
        vals = candidates(lim)
        if len(vals) >= 30:
            return vals[29]
        lim *= 10


if __name__ == "__main__":
    print(solve())
