# Problem 387: https://projecteuler.net/problem=387

from sympy import isprime


def solve(limit=10**14):
    harshads = [(digit, digit) for digit in range(1, 10)]
    total = 0

    while harshads:
        following = []
        for n, digit_sum in harshads:
            if isprime(n // digit_sum):
                for digit in (1, 3, 7, 9):
                    candidate = 10 * n + digit
                    if candidate < limit and isprime(candidate):
                        total += candidate

            for digit in range(10):
                candidate = 10 * n + digit
                candidate_sum = digit_sum + digit
                if candidate < limit // 10 and candidate % candidate_sum == 0:
                    following.append((candidate, candidate_sum))

        harshads = following

    return total


if __name__ == "__main__":
    print(solve())
