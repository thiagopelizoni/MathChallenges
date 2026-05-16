# Problem 220: https://projecteuler.net/problem=220
N = 50
STEPS = 10**12


def rot(v, r):
    x, y = v
    if r == 0:
        return x, y
    if r == 1:
        return -y, x
    if r == 2:
        return -x, -y
    return y, -x


def add(state, tr):
    x, y, r = state
    dx, dy, dr = tr
    dx, dy = rot((dx, dy), r)
    return x + dx, y + dy, (r + dr) % 4


A = [(0, 0, 0)] * (N + 1)
B = [(0, 0, 0)] * (N + 1)

for n in range(1, N + 1):
    s = add((0, 0, 0), A[n - 1])
    s = add(s, (0, 0, -1))
    s = add(s, B[n - 1])
    s = add(s, (0, 1, 0))
    A[n] = add(s, (0, 0, -1))

    s = add((0, 0, 0), (0, 0, 1))
    s = add(s, (0, 1, 0))
    s = add(s, A[n - 1])
    s = add(s, (0, 0, 1))
    B[n] = add(s, B[n - 1])


def walk(kind, n, k, pos, r):
    if k == 0 or n == 0:
        return pos, r

    full = A[n] if kind == "A" else B[n]
    if k == 2**n - 1:
        x, y, r = add((pos[0], pos[1], r), full)
        return (x, y), r

    m = 2 ** (n - 1) - 1

    if kind == "A":
        q = min(k, m)
        pos, r = walk("A", n - 1, q, pos, r)
        k -= q
        if k == 0:
            return pos, r

        r = (r - 1) % 4
        q = min(k, m)
        pos, r = walk("B", n - 1, q, pos, r)
        k -= q
        if k == 0:
            return pos, r

        dx, dy = rot((0, 1), r)
        return (pos[0] + dx, pos[1] + dy), r

    r = (r + 1) % 4
    dx, dy = rot((0, 1), r)
    pos = pos[0] + dx, pos[1] + dy
    k -= 1
    if k == 0:
        return pos, r

    q = min(k, m)
    pos, r = walk("A", n - 1, q, pos, r)
    k -= q
    if k == 0:
        return pos, r

    return walk("B", n - 1, k, pos, (r + 1) % 4)


def position(n, steps):
    pos = (0, 1)
    pos, _ = walk("A", n, steps - 1, pos, 0)
    return pos


def solve():
    x, y = position(N, STEPS)
    return f"{x},{y}"


if __name__ == "__main__":
    print(solve())
