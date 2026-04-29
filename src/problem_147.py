# Problem 147: https://projecteuler.net/problem=147


def tilted(m, n):
    ranges = [
        (max(-u, u - 2 * n), min(2 * m - u, u))
        for u in range(m + n + 1)
    ]
    total = 0

    for i, (lo1, hi1) in enumerate(ranges):
        for lo2, hi2 in ranges[i + 1:]:
            k = min(hi1, hi2) - max(lo1, lo2) + 1
            if k >= 2:
                total += k * (k - 1) // 2

    return total


def rectangles(m, n):
    return m * (m + 1) * n * (n + 1) // 4 + tilted(m, n)


def solve():
    return sum(rectangles(m, n) for m in range(1, 48) for n in range(1, 44))


if __name__ == "__main__":
    print(solve())
