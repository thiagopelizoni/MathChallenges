# Problem 786: https://projecteuler.net/problem=786

from functools import cache


@cache
def primitive_pairs(limit):
    total = 0
    for r in range(1, 9):
        if r % 3 == 0:
            continue
        height = (limit - 5 * r) // 9
        if height > 0:
            terms = (height - 1) // 5 + 1
            total += terms * height - 5 * terms * (terms - 1) // 2

    d = 2
    while d <= limit // (5 + 9):
        quotient = limit // d
        end = limit // quotient
        multiples_of_three = end // 3 - (d - 1) // 3
        count = end - d + 1 - multiples_of_three
        total -= count * primitive_pairs(quotient)
        d = end + 1
    return total


def solve(n=10**9):
    limit = (3 * (n + 2) - 1) // 2
    return 4 * primitive_pairs(limit) + 2 * (n >= 2)


if __name__ == "__main__":
    print(solve())
