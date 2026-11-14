# Problem 743: https://projecteuler.net/problem=743


def solve(k=10**8, n=10**16, mod=1_000_000_007):
    q = pow(2, n // k, mod)
    d = (q * q - 4) % mod
    prev, curr = 1, q
    fact = 1
    for i in range(2, k + 1):
        prev, curr = curr, ((2 * i - 1) * q * curr - (i - 1) ** 2 * d * prev) % mod
        fact = fact * i % mod
    return curr * pow(fact, -1, mod) % mod


if __name__ == "__main__":
    print(solve())
