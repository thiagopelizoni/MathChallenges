# Problem 491: https://projecteuler.net/problem=491

from itertools import product
from math import factorial, prod


DIGIT_SUM = 90
POSITIONS_PER_GROUP = 10


def solve():
    total = 0
    group_permutations = factorial(POSITIONS_PER_GROUP)

    for first_group_counts in product(range(3), repeat=10):
        if sum(first_group_counts) != POSITIONS_PER_GROUP:
            continue

        first_group_sum = sum(
            digit * count
            for digit, count in enumerate(first_group_counts)
        )
        if (2 * first_group_sum - DIGIT_SUM) % 11:
            continue

        first_denominator = prod(
            factorial(count) for count in first_group_counts
        )
        first_arrangements = group_permutations // first_denominator

        zero_count = first_group_counts[0]
        if zero_count:
            leading_zero_denominator = factorial(zero_count - 1) * prod(
                factorial(count) for count in first_group_counts[1:]
            )
            first_arrangements -= (
                factorial(POSITIONS_PER_GROUP - 1)
                // leading_zero_denominator
            )

        second_denominator = prod(
            factorial(2 - count) for count in first_group_counts
        )
        second_arrangements = group_permutations // second_denominator
        total += first_arrangements * second_arrangements

    return total


if __name__ == "__main__":
    print(solve())
