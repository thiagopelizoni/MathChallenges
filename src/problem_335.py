# Problem 335: https://projecteuler.net/problem=335

N = 10**18
MOD = 7**9


def m(n):
    bowls = [1] * n
    pos = 0
    moves = 0

    while True:
        beans = bowls[pos]
        bowls[pos] = 0

        for _ in range(beans):
            pos = (pos + 1) % n
            bowls[pos] += 1

        moves += 1
        if all(v == 1 for v in bowls):
            return moves


def solve():
    inv2 = pow(2, -1, MOD)
    inv3 = pow(3, -1, MOD)

    return (
        (pow(4, N + 1, MOD) - 1) * inv3
        - (pow(3, N + 1, MOD) - 1) * inv2
        + pow(2, N + 2, MOD)
        - 2
    ) % MOD


if __name__ == "__main__":
    print(solve())
