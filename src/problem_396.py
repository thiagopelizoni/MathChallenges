# Problem 396: https://projecteuler.net/problem=396

from sympy.ntheory.modular import crt


MOD = 10**9
MOD5 = 5**9
PERIOD = 4 * MOD5


def next_base(x):
    return 2 ** (x + 1) * (x + 1) - 1


def next_base_mod(x):
    if x == 0:
        x = PERIOD
    return (pow(2, x + 1, PERIOD) * (x + 1) - 1) % PERIOD


def lower_base(n):
    a0 = n % 2
    a1 = n // 2 % 2
    a2 = n // 4
    b = 2**a1 * (3 + a0) - 1
    for _ in range(a2):
        b = next_base(b)
    return b


def cubic_length(b):
    x = b
    for _ in range(b + 1):
        x = next_base_mod(x)
    return int(crt((2**9, MOD5), (-1, x % MOD5))[0]) - 2


def solve():
    bases = tuple(lower_base(n) for n in range(8))
    total = sum(b - 2 for b in bases)
    total += sum(cubic_length(b) for b in bases)
    return total % MOD


if __name__ == "__main__":
    print(solve())
