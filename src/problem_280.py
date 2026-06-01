# Problem 280: https://projecteuler.net/problem=280

from collections import deque

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve


N = 5
ALL = (1 << N) - 1
START = (12, ALL, 0, 0)
MOVES = []

for pos in range(N * N):
    x, y = pos % N, pos // N
    ns = []
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            ns.append(ny * N + nx)
    MOVES.append(ns)


def done(state):
    return state[2] == ALL and state[3] == 0


def advance(state, pos):
    _, bottom, top, carry = state
    x, y = pos % N, pos // N

    if carry:
        if y == N - 1 and not (top >> x) & 1:
            return pos, bottom, top | (1 << x), 0
        return pos, bottom, top, carry

    if y == 0 and (bottom >> x) & 1:
        return pos, bottom & ~(1 << x), top, 1
    return pos, bottom, top, carry


def states():
    idx = {START: 0}
    out = [START]
    q = deque([START])

    while q:
        state = q.popleft()
        for pos in MOVES[state[0]]:
            nxt = advance(state, pos)
            if not done(nxt) and nxt not in idx:
                idx[nxt] = len(out)
                out.append(nxt)
                q.append(nxt)

    return out, idx


def solve():
    st, idx = states()
    rows = []
    cols = []
    vals = []

    for i, state in enumerate(st):
        rows.append(i)
        cols.append(i)
        vals.append(1.0)

        p = 1.0 / len(MOVES[state[0]])
        for pos in MOVES[state[0]]:
            nxt = advance(state, pos)
            if not done(nxt):
                rows.append(i)
                cols.append(idx[nxt])
                vals.append(-p)

    a = csr_matrix((vals, (rows, cols)), shape=(len(st), len(st)))
    e = spsolve(a, np.ones(len(st)))
    return f"{e[0]:.6f}"


if __name__ == "__main__":
    print(solve())
