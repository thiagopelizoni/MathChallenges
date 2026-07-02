# Problem 355: https://projecteuler.net/problem=355

from bisect import bisect_right
from collections import deque
from math import isqrt

from sympy import sieve


N = 200_000


def add_edge(g, u, v, cap, cost):
    g[u].append([v, cap, cost, len(g[v])])
    g[v].append([u, 0, -cost, len(g[u]) - 1])


def min_cost(g, source, sink, need):
    total = 0
    n = len(g)

    for _ in range(need):
        dist = [float("inf")] * n
        active = [False] * n
        prev_v = [-1] * n
        prev_e = [-1] * n
        dist[source] = 0
        q = deque([source])
        active[source] = True

        while q:
            u = q.popleft()
            active[u] = False

            for i, e in enumerate(g[u]):
                v, cap, cost = e[:3]
                if cap and dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    prev_v[v] = u
                    prev_e[v] = i
                    if not active[v]:
                        q.append(v)
                        active[v] = True

        total += dist[sink]
        v = sink
        while v != source:
            u = prev_v[v]
            e = g[u][prev_e[v]]
            e[1] -= 1
            g[v][e[3]][1] += 1
            v = u

    return total


def max_power(p, n):
    x = p

    while x * p <= n:
        x *= p

    return x


def gains_by_prime(n, small, large):
    s = len(small)
    index = {}
    gains = [{} for _ in small]

    for i, p in enumerate(small):
        m = p
        while m * large[0] <= n:
            end = bisect_right(large, n // m)
            for q in large[max(0, end - s) : end]:
                j = index.setdefault(q, len(index))
                gain = q * (m - 1)
                if gain > gains[i].get(j, 0):
                    gains[i][j] = gain
            m *= p

    return index, gains


def matching_gain(n, small, large):
    large_index, gains = gains_by_prime(n, small, large)
    s = len(small)
    source = 0
    p0 = 1
    q0 = p0 + s
    sink = q0 + len(large_index)
    g = [[] for _ in range(sink + 1)]

    for i, p in enumerate(small):
        add_edge(g, source, p0 + i, 1, 0)
        add_edge(g, p0 + i, sink, 1, -max_power(p, n))
        for j, gain in gains[i].items():
            add_edge(g, p0 + i, q0 + j, 1, -gain)

    for j in large_index.values():
        add_edge(g, q0 + j, sink, 1, 0)

    return -min_cost(g, source, sink, s)


def co(n):
    root = isqrt(n)
    small = list(sieve.primerange(2, root + 1))
    large = list(sieve.primerange(root + 1, n + 1))
    return 1 + sum(large) + matching_gain(n, small, large)


def solve():
    return co(N)


if __name__ == "__main__":
    print(solve())
