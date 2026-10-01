# Problem 648: https://projecteuler.net/problem=648

from sympy.discrete.convolutions import convolution_int


def solve(n=1000):
    mod = 10**9
    p = [1, mod - 1][:n + 1]
    factor = [0, 1, mod - 1][:n + 1]
    total = sum(p)

    for j in range(1, n + 1):
        p = convolution_int(p, factor)[:n + 1]
        p = [c % mod for c in p]
        total = (total + sum(p)) % mod

        factor = convolution_int(factor, [1, -2, 1])[:n + 1]
        factor[1] += 1
        if n >= 2:
            factor[2] -= 1
        factor = [c % mod for c in factor]

    return total % mod


if __name__ == "__main__":
    print(solve())
