# Problem 774: https://projecteuler.net/problem=774

from functools import cache


def count(n, b, mod):
    fib = [0, 1]
    for _ in range(n + 1):
        fib.append((fib[-1] + fib[-2]) % mod)

    @cache
    def paths(limit, left, right, edges):
        if edges == 1:
            return int((left & right) == 0)
        if limit == 0:
            return 0
        if limit % 2 == 0:
            high = paths(limit // 2, left // 2, right // 2, edges)
            index = edges + 1 - left % 2 - right % 2
            return high * fib[index] % mod

        last = limit - 1
        total = paths(last, left, right, edges)
        for gap in range(1, edges):
            total += paths(last, left, last, gap) * paths(limit, last, right, edges - gap)
        return total % mod

    ways = [1]
    blocks = []
    for length in range(1, n + 1):
        block = paths(b + 1, 0, 0, length + 1)
        blocks.append(block if length % 2 else -block)
        total = sum(weight * prefix for weight, prefix in zip(blocks, reversed(ways)))
        ways.append(total % mod)
    return ways[-1]


def solve():
    return count(123, 123456789, 998244353)


if __name__ == "__main__":
    print(solve())
