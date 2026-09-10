# Problem 603: https://projecteuler.net/problem=603

from sympy import sieve


def substring_sum(digits, k, mod):
    n = len(digits)
    value = weighted = digit_sum = position_sum = 0
    for i, char in enumerate(digits, 1):
        d = int(char)
        value = (10 * value + d) % mod
        weighted = (10 * weighted + i * d) % mod
        digit_sum += d
        position_sum += i * d

    q = pow(10, n, mod)
    pairs = k * (k - 1) // 2
    if q == 1:
        geometric = k % mod
        shifted = pairs % mod
    else:
        inverse = pow(q - 1, -1, mod)
        geometric = (pow(q, k, mod) - 1) * inverse % mod
        shifted = (geometric - k) * inverse % mod

    total = 10 * (weighted * geometric + n * value * shifted)
    total -= k * position_sum + n * digit_sum * pairs
    return total * pow(9, -1, mod) % mod


def solve():
    n = 10**6
    k = 10**12
    mod = 10**9 + 7
    sieve.extend_to_no(n)
    digits = "".join(str(p) for p in sieve[1:n + 1])
    return substring_sum(digits, k, mod)


if __name__ == "__main__":
    print(solve())
