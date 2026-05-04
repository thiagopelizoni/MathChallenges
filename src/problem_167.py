# Problem 167: https://projecteuler.net/problem=167


def period_ones(b):
    span = b + 1
    initial = (1 << span) - 1
    state = initial
    ones = []
    i = 0

    while True:
        if state & 1:
            ones.append(i)

        new = (state ^ (state >> (span - 1))) & 1
        state = (state >> 1) | (new << (span - 1))
        i += 1
        if state == initial:
            return i, ones


def ulam_value(b, k):
    period, ones = period_ones(b)
    q = k - 2
    cycles, r = divmod(q - 1, len(ones))
    return b + 2 * (cycles * period + ones[r])


def solve():
    k = 10**11
    return sum(ulam_value(2 * n + 1, k) for n in range(2, 11))


if __name__ == "__main__":
    print(solve())
