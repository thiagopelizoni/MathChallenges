# Problem 400: https://projecteuler.net/problem=400

from array import array


MOD = 10**18


def grundy_values(k):
    g = [0, 1]
    for _ in range(2, k + 1):
        g.append(1 + (g[-1] ^ g[-2]))
    return g


def winning_moves(k):
    g = grundy_values(k)
    needed = [None] * k
    pending = {k - 1: {g[k - 2]}, k - 2: {g[k - 1]}}

    for n in range(k - 1, -1, -1):
        values = pending.pop(n, set())
        needed[n] = array("I", sorted(values))
        if n < 2:
            continue

        left = pending.setdefault(n - 1, set())
        right = pending.setdefault(n - 2, set())
        for t in values:
            if t:
                left.add((t - 1) ^ g[n - 2])
                right.add((t - 1) ^ g[n - 1])

    prev2 = {t: 0 for t in needed[0]}
    prev1 = {t: int(t == 0) for t in needed[1]}

    for n in range(2, k):
        cur = {}
        for t in needed[n]:
            if t == 0:
                cur[t] = 1
            else:
                cur[t] = (
                    prev1[(t - 1) ^ g[n - 2]]
                    + prev2[(t - 1) ^ g[n - 1]]
                ) % MOD
        prev2, prev1 = prev1, cur

    return (prev1[g[k - 2]] + prev2[g[k - 1]]) % MOD


def solve():
    return winning_moves(10_000)


if __name__ == "__main__":
    print(solve())
