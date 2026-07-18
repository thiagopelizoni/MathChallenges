# Problem 412: https://projecteuler.net/problem=412

MOD = 76_543_217
M = 10_000
N = 5_000


def count_numberings(m, n, mod):
    side = m - n
    cells = m * m - n * n
    limit = 2 * m
    fact = [1] * (limit + 1)

    for k in range(1, limit + 1):
        fact[k] = fact[k - 1] * k % mod

    inv_fact = [1] * (limit + 1)
    inv_fact[limit] = pow(fact[limit], -1, mod)
    for k in range(limit, 0, -1):
        inv_fact[k - 1] = inv_fact[k] * k % mod

    hooks = 1
    for i in range(1, side + 1):
        square = fact[2 * m - i] * inv_fact[2 * m - i - side] % mod
        arm = fact[m - i] * inv_fact[m - i - n] % mod
        hooks = hooks * square * arm * arm % mod

    tail = 1
    for k in range(cells + 1, mod):
        tail = tail * k % mod
    cells_factorial = -pow(tail, -1, mod) % mod

    return cells_factorial * pow(hooks, -1, mod) % mod


def solve():
    return count_numberings(M, N, MOD)


if __name__ == "__main__":
    print(solve())
