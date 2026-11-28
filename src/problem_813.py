# Problem 813: https://projecteuler.net/problem=813


def solve():
    mod = 10**9 + 7
    n = 8**12 * 12**8
    spacing = 1
    while n % 2 == 0:
        n //= 2
        spacing *= 2

    coeffs = 1
    stride = 1
    while n:
        if n % 2:
            coeffs ^= (coeffs << stride) ^ (coeffs << (3 * stride))
        stride *= 2
        n //= 2

    base = pow(2, spacing, mod)
    value = 0
    for digit in format(coeffs, "b"):
        value = (value * base + int(digit)) % mod
    return value


if __name__ == "__main__":
    print(solve())
