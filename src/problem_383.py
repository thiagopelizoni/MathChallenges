# Problem 383: https://projecteuler.net/problem=383

from collections import defaultdict


def solve(n=10**18):
    digits = []
    value = n
    while value:
        digits.append(value % 5)
        value //= 5

    states = {(-1, 1, 0, False): 1}
    for bound in digits:
        nxt = defaultdict(int)
        for (carry, difference, comparison, positive), ways in states.items():
            for digit in range(5):
                doubled = 2 * digit + carry
                if digit < bound:
                    new_comparison = -1
                elif digit > bound:
                    new_comparison = 1
                else:
                    new_comparison = comparison

                state = (
                    doubled // 5,
                    difference + doubled % 5 - 2 * digit,
                    new_comparison,
                    positive or digit > 0,
                )
                nxt[state] += ways
        states = nxt

    return sum(
        ways
        for (carry, difference, comparison, positive), ways in states.items()
        if positive and comparison <= 0 and difference + carry > 0
    )


if __name__ == "__main__":
    print(solve())
