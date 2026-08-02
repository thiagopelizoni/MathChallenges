# Problem 488: https://projecteuler.net/problem=488

from functools import cache
from itertools import product


N = 10**18
MOD = 10**9
HALVES = ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0))


def bounded_sum(bounds):
    scale = 1
    while scale <= max(bounds):
        scale *= 2
    scale //= 2

    @cache
    def visit(a, b, c, scale):
        if scale == 0:
            return 1, 0
        count = total = 0
        for halves in HALVES:
            reduced = []
            for bound, upper in zip((a, b, c), halves):
                if upper and bound < scale:
                    break
                reduced.append(
                    bound - scale if upper else min(bound, scale - 1)
                )
            else:
                partial_count, partial_total = visit(
                    *reduced, scale // 2
                )
                count += partial_count
                total += (
                    partial_total
                    + partial_count * scale * sum(halves)
                )
        return count, total

    return visit(*bounds, scale)


def losing_sum(n):
    count = total = 0
    for restricted in product((False, True), repeat=3):
        bounds = tuple(1 if flag else n for flag in restricted)
        partial_count, partial_total = bounded_sum(bounds)
        sign = -1 if sum(restricted) % 2 else 1
        count += sign * partial_count
        total += sign * partial_total
    return (total - 3 * count) // 6


def solve():
    return f"{losing_sum(N) % MOD:09d}"


if __name__ == "__main__":
    print(solve())
