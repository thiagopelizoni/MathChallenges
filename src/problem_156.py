# Problem 156: https://projecteuler.net/problem=156


def count_digit(n, d):
    if n <= 0:
        return 0

    total = 0
    p = 1
    while p <= n:
        high = n // (10 * p)
        cur = (n // p) % 10
        low = n % p

        if cur > d:
            total += (high + 1) * p
        elif cur == d:
            total += high * p + low + 1
        else:
            total += high * p
        p *= 10

    return total


def roots(d):
    ans = []
    stack = [(0, 10**12)]

    while stack:
        lo, hi = stack.pop()
        if count_digit(hi, d) < lo or count_digit(lo, d) > hi:
            continue

        if lo == hi:
            if count_digit(lo, d) == lo:
                ans.append(lo)
            continue

        step = (hi - lo + 10) // 10
        for start in range(lo, hi + 1, step):
            stack.append((start, min(hi, start + step - 1)))

    return ans


def solve():
    return sum(sum(roots(d)) for d in range(1, 10))


if __name__ == "__main__":
    print(solve())
