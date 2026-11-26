# Problem 806: https://projecteuler.net/problem=806
from itertools import product


def solve(n=10**5):
    mod = 1_000_000_007
    if n % 2:
        return 0

    half = n // 2
    fact = [1] * (half + 1)
    twos = [1] * (half + 1)
    for i in range(1, half + 1):
        fact[i] = fact[i - 1] * i % mod
        twos[i] = twos[i - 1] * 2 % mod
    invfact = [1] * (half + 1)
    invfact[half] = pow(fact[half], -1, mod)
    for i in range(half, 0, -1):
        invfact[i - 1] = invfact[i] * i % mod

    def coefficient(a, b, c):
        if a % 2 != b % 2 or b % 2 != c % 2:
            return 0
        total = 0
        for k in range(a % 2, min(a, b, c) + 1, 2):
            i, j, h = (a - k) // 2, (b - k) // 2, (c - k) // 2
            ways = fact[i + j + h + k] * invfact[k] % mod
            ways = ways * invfact[i] * invfact[j] % mod
            total += ways * invfact[h] * twos[k] % mod
        return total % mod

    bits = [1 << i for i in range(half.bit_length()) if half & (1 << i)]
    losing = 0
    for missing in product(range(3), repeat=len(bits)):
        heaps = [half, half, half]
        for peg, bit in zip(missing, bits):
            heaps[peg] -= bit
        a, b, c = heaps
        losing += coefficient(a, b, c) + 2 * coefficient(a - 1, b, c)
        losing += 2 * coefficient(a - 1, b - 1, c) - coefficient(a - 2, b, c)

    return losing * (pow(2, n, mod) - 1) * pow(2, -1, mod) % mod


if __name__ == "__main__":
    print(solve())
