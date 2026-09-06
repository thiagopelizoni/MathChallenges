# Problem 592: https://projecteuler.net/problem=592

from math import factorial


def solve(n=factorial(20), digits=12):
    mod = 16**digits
    block = 2
    while block**3 < mod:
        block *= 2

    prefix = [(1, 0, 0)]
    p, s, t = prefix[0]
    for i in range(1, block, 2):
        inv = pow(i, -1, mod)
        t = (t + s * inv) % mod
        s = (s + inv) % mod
        p = p * i % mod
        prefix.append((p, s, t))

    full = p
    a = block * s % mod
    b = block**2 * t % mod
    ans = 1
    e = 0
    while n:
        q, r = divmod(n, block)
        s = q * (q - 1) // 2
        t = q * (q - 1) * (2 * q - 1) // 6
        pairs = (s * s - t) // 2
        correction = (1 + a * s + b * t + a * a * pairs) % mod
        ans = ans * pow(full, q, mod) * correction % mod

        p, s, t = prefix[(r + 1) // 2]
        offset = q * block
        tail = p * (1 + offset * s + offset**2 * t) % mod
        ans = ans * tail % mod
        n //= 2
        e += n

    ans = ans * 2 ** (e % 4) % mod
    return f"{ans:0{digits}X}"


if __name__ == "__main__":
    print(solve())
