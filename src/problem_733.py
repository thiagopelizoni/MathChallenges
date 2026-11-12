# Problem 733: https://projecteuler.net/problem=733


def solve(n=10**6, mod=1_000_000_007):
    a = []
    x = 1
    for _ in range(n):
        x = x * 153 % 10_000_019
        a.append(x)

    order = {x: i for i, x in enumerate(sorted(set(a)))}
    ranks = [order[x] for x in a]
    size = 1
    while size < len(order):
        size *= 2
    del order

    counts = [1] * n
    totals = a
    for _ in range(2, 5):
        tree_c = [0] * (2 * size)
        tree_s = [0] * (2 * size)
        next_c = [0] * n
        next_s = [0] * n
        for i, x in enumerate(a):
            p = size + ranks[i]
            c = s = 0
            while p > 1:
                if p % 2:
                    c += tree_c[p - 1]
                    s += tree_s[p - 1]
                p //= 2
            next_c[i] = c % mod
            next_s[i] = (s + x * c) % mod

            c, s = counts[i], totals[i]
            p = size + ranks[i]
            while p:
                tree_c[p] = (tree_c[p] + c) % mod
                tree_s[p] = (tree_s[p] + s) % mod
                p //= 2
        counts, totals = next_c, next_s

    return sum(totals) % mod


if __name__ == "__main__":
    print(solve())
