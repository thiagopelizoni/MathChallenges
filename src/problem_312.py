# Problem 312: https://projecteuler.net/problem=312

from sympy.ntheory.modular import crt


N = 10_000
MOD = 13**8


def c_small(n, mod):
    if n <= 2:
        return 1 % mod

    e = 3 ** (n - 2)
    return pow(2, e, mod) * pow(3, (e - 3) // 2, mod) % mod


def exp_mod(n, q):
    r = pow(3, (n - 2) % (12 * 13 ** (q - 1)), 13**q)
    return int(crt([8, 3, 13**q], [1, 0, r])[0] % (24 * 13**q))


def c_from_residue(n, q):
    mod = 13 ** (q + 1)
    phi = 12 * 13**q
    e = exp_mod(n, q)
    r = pow(2, e % phi, mod) * pow(3, ((e - 3) // 2) % phi, mod) % mod
    return int(crt([4, 3, mod], [0, 0, r])[0] % (12 * mod))


def solve():
    a = c_small(N, 12 * 13**4)
    b = c_from_residue(a, 5)
    e = exp_mod(b, 7)
    phi = 12 * 13**7

    return pow(2, e % phi, MOD) * pow(3, ((e - 3) // 2) % phi, MOD) % MOD


if __name__ == "__main__":
    print(solve())
