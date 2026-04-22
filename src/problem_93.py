# Problem 93: https://projecteuler.net/problem=93

from fractions import Fraction
from functools import cache
from itertools import combinations


@cache
def values(nums):
    if len(nums) == 1:
        return {nums[0]}

    ans = set()
    n = len(nums)
    for mask in range(1, (1 << n) - 1):
        left = tuple(nums[i] for i in range(n) if mask >> i & 1)
        right = tuple(nums[i] for i in range(n) if not mask >> i & 1)

        for a in values(left):
            for b in values(right):
                ans.add(a + b)
                ans.add(a - b)
                ans.add(b - a)
                ans.add(a * b)
                if b:
                    ans.add(a / b)
                if a:
                    ans.add(b / a)

    return ans


def run_length(digits):
    nums = tuple(Fraction(d) for d in digits)
    made = {int(x) for x in values(nums) if x.denominator == 1 and x > 0}

    n = 1
    while n in made:
        n += 1
    return n - 1


def solve():
    best = max(combinations(range(1, 10), 4), key=run_length)
    return "".join(map(str, best))


if __name__ == "__main__":
    print(solve())
