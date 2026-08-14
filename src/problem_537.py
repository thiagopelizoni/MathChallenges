# Problem 537: https://projecteuler.net/problem=537

from sympy import prime, primerange
from sympy.discrete.transforms import intt, ntt


N = 20_000
MOD = 1_004_535_809


def convolve(a, b):
    length = min(len(a) + len(b) - 1, N + 1)
    size = 1
    while size < len(a) + len(b) - 1:
        size *= 2
    x = ntt(a + [0] * (size - len(a)), MOD)
    y = ntt(b + [0] * (size - len(b)), MOD)
    return intt([u * v % MOD for u, v in zip(x, y)], MOD)[:length]


def solve():
    ps = list(primerange(2, prime(N + 1) + 1))
    base = [1] + [q - p for p, q in zip(ps, ps[1:])]
    result = [1]
    exponent = N
    while exponent:
        if exponent % 2:
            result = convolve(result, base)
        exponent //= 2
        if exponent:
            base = convolve(base, base)
    return result[N]


if __name__ == "__main__":
    print(solve())
