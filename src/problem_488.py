# Problem 488: https://projecteuler.net/problem=488

from itertools import product


N = 10**18
MOD = 10**9


def bounded_xor_sum(bounds):
    states = {(True, True, True): (1, 0)}
    for shift in range(max(bounds).bit_length() - 1, -1, -1):
        limits = tuple((bound >> shift) & 1 for bound in bounds)
        place = 1 << shift
        following = {}
        for tight, (count, total) in states.items():
            for xbit, ybit in product((0, 1), repeat=2):
                digits = (xbit, ybit, xbit ^ ybit)
                if any(
                    flag and digit > limit
                    for flag, digit, limit in zip(tight, digits, limits)
                ):
                    continue
                key = tuple(
                    flag and digit == limit
                    for flag, digit, limit in zip(tight, digits, limits)
                )
                old_count, old_total = following.get(key, (0, 0))
                following[key] = (
                    old_count + count,
                    old_total + total + count * place * sum(digits),
                )
        states = following
    return (
        sum(count for count, _ in states.values()),
        sum(total for _, total in states.values()),
    )


def losing_sum(n):
    count = total = 0
    for restricted in product((False, True), repeat=3):
        bounds = tuple(1 if flag else n for flag in restricted)
        partial_count, partial_total = bounded_xor_sum(bounds)
        sign = -1 if sum(restricted) % 2 else 1
        count += sign * partial_count
        total += sign * partial_total
    return (total - 3 * count) // 6


def solve():
    return f"{losing_sum(N) % MOD:09d}"


if __name__ == "__main__":
    print(solve())
