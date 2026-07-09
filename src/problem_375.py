# Problem 375: https://projecteuler.net/problem=375

from array import array

from sympy import n_order


START = 290797
MOD = 50515093
N = 2_000_000_000


def period_len():
    order = n_order(START, MOD)
    while order % 2 == 0:
        order //= 2
    return n_order(2, order)


def sequence_period():
    s = START
    seq = array("I")
    for _ in range(period_len()):
        s = s * s % MOD
        seq.append(s)
    return seq


def capped_pairs(left, right, cap):
    if left <= 0 or right <= 0 or cap <= 0:
        return 0
    if cap >= left + right - 1:
        return left * right

    amax = min(left, cap)
    full = min(amax, max(0, cap + 1 - right))
    rem = amax - full
    return full * right + rem * (cap + 1) - (full + 1 + amax) * rem // 2


def stack_sum(period, n, cap, start_limit=None):
    size = len(period)
    stack = array("i")
    total = 0

    def value(i):
        return period[i] if i < size else period[i - size]

    for i in range(n + 1):
        cur = -1 if i == n else value(i)
        while stack and value(stack[-1]) >= cur:
            j = stack.pop()
            prev = stack[-1] if stack else -1
            left = j - prev
            right = i - j

            if start_limit is None:
                ways = capped_pairs(left, right, cap)
            else:
                lo = max(1, j - start_limit + 2)
                ways = 0
                if lo <= left:
                    ways = capped_pairs(left, right, cap) - capped_pairs(lo - 1, right, cap)

            total += value(j) * ways

        if i < n:
            stack.append(i)

    return total


def m(n):
    period = sequence_period()
    size = len(period)
    if n < size:
        return stack_sum(period, n, n)

    q, r = divmod(n, size)
    circular = stack_sum(period, 2 * size - 1, size - 1, start_limit=size)
    tail = stack_sum(period, size + r, size - 1)
    short = (q - 1) * circular + tail
    short_count = (size - 1) * (n + 1) - size * (size - 1) // 2
    total_count = n * (n + 1) // 2
    return short + min(period) * (total_count - short_count)


def solve():
    return m(N)


if __name__ == "__main__":
    print(solve())
