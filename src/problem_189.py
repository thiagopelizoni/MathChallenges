# Problem 189: https://projecteuler.net/problem=189
from collections import defaultdict


def triangles(n):
    out = []
    for i in range(n):
        for j in range(n - i):
            out.append(tuple(sorted(((i, j), (i + 1, j), (i, j + 1)))))
    for i in range(n - 1):
        for j in range(n - 1 - i):
            out.append(tuple(sorted(((i + 1, j), (i, j + 1), (i + 1, j + 1)))))
    return out


def adjacency(tris):
    by_edge = defaultdict(list)
    for i, t in enumerate(tris):
        for a, b in ((t[0], t[1]), (t[0], t[2]), (t[1], t[2])):
            by_edge[a, b].append(i)

    adj = [set() for _ in tris]
    for edge in by_edge.values():
        if len(edge) == 2:
            a, b = edge
            adj[a].add(b)
            adj[b].add(a)
    return [tuple(s) for s in adj]


def count_colourings(n):
    tris = triangles(n)
    adj = adjacency(tris)
    order = sorted(
        range(len(tris)),
        key=lambda i: (
            sum(x + y for x, y in tris[i]),
            sum(x for x, _ in tris[i]),
            sum(y for _, y in tris[i]),
        ),
    )
    pos = {v: i for i, v in enumerate(order)}
    last = [max([pos[v]] + [pos[w] for w in adj[v]]) for v in range(len(tris))]

    dp = {(): 1}
    for t, v in enumerate(order):
        before = tuple(u for u in order[:t] if last[u] >= t)
        after = tuple(u for u in order[: t + 1] if last[u] >= t + 1)
        idx = {u: i for i, u in enumerate(before)}
        previous = [u for u in adj[v] if pos[u] < t]
        nxt = defaultdict(int)

        for state, cnt in dp.items():
            used = {state[idx[u]] for u in previous}
            colors = {u: state[i] for i, u in enumerate(before)}
            for c in range(3):
                if c in used:
                    continue
                colors[v] = c
                nxt[tuple(colors[u] for u in after)] += cnt
        dp = nxt

    return dp[()]


def solve():
    return count_colourings(8)


if __name__ == "__main__":
    print(solve())
