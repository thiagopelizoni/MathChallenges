# Problem 776: https://projecteuler.net/problem=776
from fractions import Fraction


def f(n):
    dp = {(0, True): (1, 0)}
    for digit in map(int, str(n)):
        next_dp = {}
        for (s, tight), (count, total) in dp.items():
            stop = digit if tight else 9
            for d in range(stop + 1):
                key = s + d, tight and d == digit
                c, t = next_dp.get(key, (0, 0))
                next_dp[key] = c + count, t + 10 * total + d * count
        dp = next_dp

    return sum(Fraction(total, s) for (s, _), (_, total) in dp.items() if s)


def solve():
    ans = f(1234567890123456789)
    mantissa, exponent = format(ans, ".12e").split("e")
    return f"{mantissa}e{int(exponent)}"


if __name__ == "__main__":
    print(solve())
