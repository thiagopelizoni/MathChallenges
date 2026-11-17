# Problem 760: https://projecteuler.net/problem=760

from itertools import product


def solve(n=10**18):
    mod = 1_000_000_007
    dp = {0: (1, 0)}
    for i in range(n.bit_length()):
        bit = (n >> i) & 1
        weight = 1 << i
        nxt = {}
        for carry, (count, total) in dp.items():
            for a, b, c in product((0, 1), repeat=3):
                q, r = divmod(a + b + c + carry, 2)
                if r != bit:
                    continue
                ways, value = nxt.get(q, (0, 0))
                ways += count
                value += total + count * 2 * (a | b) * weight
                nxt[q] = (ways % mod, value % mod)
        dp = nxt
    return dp[0][1]


if __name__ == "__main__":
    print(solve())
