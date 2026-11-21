# Problem 781: https://projecteuler.net/problem=781

from math import factorial


def multiply(a, b, size, mod):
    bound = min(len(a), len(b)) * (mod - 1) ** 2
    width = 1
    while bound >= 256:
        bound //= 256
        width += 1

    def pack(poly):
        digits = b"".join(c.to_bytes(width, "little") for c in poly)
        return int.from_bytes(digits, "little")

    product = pack(a) * pack(b)
    digits = product.to_bytes((len(a) + len(b) - 1) * width, "little")
    return [
        int.from_bytes(digits[i:i + width], "little") % mod
        for i in range(0, size * width, width)
    ]


def solve():
    n = 50_000
    mod = 1_000_000_007

    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(factorial(n), -1, mod)
    for j in range(n, 0, -1):
        inv_fact[j - 1] = j * inv_fact[j] % mod

    closed = []
    opened = []
    deranged = with_path = 0
    sign = matchings = 1
    for j, term in enumerate(inv_fact):
        deranged = (deranged + sign * term) % mod
        with_path = (with_path + deranged) % mod
        if j % 2 == 0:
            closed.append(matchings * deranged % mod)
            opened.append(matchings * with_path % mod)
            matchings = matchings * (j + 1) % mod
        sign = -sign

    inverse = [1]
    while len(inverse) < len(closed):
        size = min(2 * len(inverse), len(closed))
        correction = multiply(closed[:size], inverse, size, mod)
        correction = [-c % mod for c in correction]
        correction[0] = (correction[0] + 2) % mod
        inverse = multiply(inverse, correction, size, mod)

    return sum(a * b for a, b in zip(opened, reversed(inverse))) % mod


if __name__ == "__main__":
    print(solve())
