# Problem 767: https://projecteuler.net/problem=767

from sympy import convolution


def count_blocks(k, blocks):
    rows = 16
    mod = 1_000_000_007
    fact = [1]
    for i in range(1, k + 1):
        fact.append(fact[-1] * i % mod)

    invfact = [1] * (k + 1)
    invfact[k] = pow(fact[k], -1, mod)
    for i in range(k, 0, -1):
        invfact[i - 1] = invfact[i] * i % mod

    coeffs = [pow(x, rows, mod) for x in invfact]
    pairs = convolution(coeffs, coeffs)
    extra = (pow(2, blocks, mod) - 2) % mod
    total = 0
    weight = 1
    for j in range(k + 1):
        m = k - j
        choices = fact[k] * invfact[j] * invfact[m] % mod
        row_ways = pow(fact[m], rows, mod) * pairs[m] % mod
        total = (total + choices * weight * row_ways) % mod
        weight = weight * extra % mod
    return total


def solve():
    k = 10**5
    return count_blocks(k, 10**16 // k)


if __name__ == "__main__":
    print(solve())
