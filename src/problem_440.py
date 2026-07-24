# Problem 440: https://projecteuler.net/problem=440

from sympy import sieve, sqrt_mod


L = 2000
MOD = 987_898_789


def solve():
    mu = tuple(sieve.mobiusrange(1, L + 1))
    coprime_odd = [
        sum(mu[d - 1] * ((n // d + 1) // 2) ** 2 for d in range(1, n + 1, 2))
        for n in range(L + 1)
    ]
    counts = [coprime_odd[L // g] for g in range(1, L + 1)]
    rest = L * L - sum(counts)

    root = sqrt_mod(104, MOD)
    half = pow(2, -1, MOD)
    alpha = (10 + root) * half % MOD
    beta = (10 - root) * half % MOD
    scale = pow(root, -1, MOD)

    total = 0
    for c in range(1, L + 1):
        x = pow(alpha, c, MOD)
        y = pow(beta, c, MOD)
        subtotal = rest * (10 if c % 2 else 1)
        for count in counts:
            subtotal += count * (alpha * x - beta * y) * scale % MOD
            x = pow(x, c, MOD)
            y = pow(y, c, MOD)
        total = (total + subtotal) % MOD
    return total


if __name__ == "__main__":
    print(solve())
