# Problem 680: https://projecteuler.net/problem=680

import random


def solve():
    n = 10**18
    k_ops = 10**6
    mod = 10**9

    max_nodes = 2 * k_ops + 2
    left = [0] * max_nodes
    right = [0] * max_nodes
    sz = [0] * max_nodes
    length = [0] * max_nodes
    first = [0] * max_nodes
    last = [0] * max_nodes
    rev = [0] * max_nodes

    rng = random.Random(0)
    prio = [rng.random() for _ in range(max_nodes)]
    prio[0] = -1.0

    sz[1] = n
    length[1] = n
    first[1] = 0
    last[1] = n - 1
    nxt = 2
    root = 1

    def split(u, k):
        nonlocal nxt
        right[0] = 0
        left[0] = 0
        l_tail = 0
        r_tail = 0

        while u:
            if rev[u]:
                first[u], last[u] = last[u], first[u]
                lu = left[u]
                ru = right[u]
                left[u] = ru
                right[u] = lu
                rev[lu] = 1 - rev[lu]
                rev[ru] = 1 - rev[ru]
                rev[u] = 0

            lu = left[u]
            lsz = sz[lu]
            ulen = length[u]

            if k <= lsz:
                sz[u] -= k
                left[r_tail] = u
                r_tail = u
                u = lu
            elif k >= lsz + ulen:
                sz[u] = k
                k -= lsz + ulen
                right[l_tail] = u
                l_tail = u
                u = right[u]
            else:
                off = k - lsz
                v = nxt
                nxt += 1
                f = first[u]
                la = last[u]
                if f <= la:
                    last[u] = f + off - 1
                    first[v] = f + off
                    last[v] = la
                else:
                    last[u] = f - off + 1
                    first[v] = f - off
                    last[v] = la
                length[u] = off
                length[v] = ulen - off
                ru = right[u]
                right[v] = ru
                sz[v] = sz[u] - k
                sz[u] = k
                right[l_tail] = u
                l_tail = u
                left[r_tail] = v
                r_tail = v
                break

        right[l_tail] = 0
        left[r_tail] = 0
        return right[0], left[0]

    def merge(l, r):
        if not l or not r:
            return l or r
        if prio[l] > prio[r]:
            head = l
            while True:
                if rev[l]:
                    first[l], last[l] = last[l], first[l]
                    lu = left[l]
                    ru = right[l]
                    left[l] = ru
                    right[l] = lu
                    rev[lu] = 1 - rev[lu]
                    rev[ru] = 1 - rev[ru]
                    rev[l] = 0
                sz[l] += sz[r]
                nl = right[l]
                if prio[nl] > prio[r]:
                    l = nl
                else:
                    right[l] = r
                    l = nl
                    if not l:
                        break
                    while True:
                        if rev[r]:
                            first[r], last[r] = last[r], first[r]
                            lu = left[r]
                            ru = right[r]
                            left[r] = ru
                            right[r] = lu
                            rev[lu] = 1 - rev[lu]
                            rev[ru] = 1 - rev[ru]
                            rev[r] = 0
                        sz[r] += sz[l]
                        nr = left[r]
                        if prio[nr] > prio[l]:
                            r = nr
                        else:
                            left[r] = l
                            r = nr
                            break
                    if not r:
                        break
            return head
        else:
            head = r
            while True:
                if rev[r]:
                    first[r], last[r] = last[r], first[r]
                    lu = left[r]
                    ru = right[r]
                    left[r] = ru
                    right[r] = lu
                    rev[lu] = 1 - rev[lu]
                    rev[ru] = 1 - rev[ru]
                    rev[r] = 0
                sz[r] += sz[l]
                nr = left[r]
                if prio[nr] > prio[l]:
                    r = nr
                else:
                    left[r] = l
                    r = nr
                    if not r:
                        break
                    while True:
                        if rev[l]:
                            first[l], last[l] = last[l], first[l]
                            lu = left[l]
                            ru = right[l]
                            left[l] = ru
                            right[l] = lu
                            rev[lu] = 1 - rev[lu]
                            rev[ru] = 1 - rev[ru]
                            rev[l] = 0
                        sz[l] += sz[r]
                        nl = right[l]
                        if prio[nl] > prio[r]:
                            l = nl
                        else:
                            right[l] = r
                            l = nl
                            break
                    if not l:
                        break
            return head

    f1 = 1
    f2 = 1
    for _ in range(k_ops):
        s = f1
        t = f2
        f1 = (f1 + f2) % n
        f2 = (f1 + f2) % n
        if s == t:
            continue
        if s > t:
            s, t = t, s

        p1, p23 = split(root, s)
        p2, p3 = split(p23, t - s + 1)
        rev[p2] = 1 - rev[p2]
        root = merge(p1, merge(p2, p3))

    ans = 0
    pos = 0
    stack = []
    curr = root
    while stack or curr:
        while curr:
            if rev[curr]:
                first[curr], last[curr] = last[curr], first[curr]
                lu = left[curr]
                ru = right[curr]
                left[curr] = ru
                right[curr] = lu
                rev[lu] = 1 - rev[lu]
                rev[ru] = 1 - rev[ru]
                rev[curr] = 0
            stack.append(curr)
            curr = left[curr]
        curr = stack.pop()
        f = first[curr]
        la = last[curr]
        ln = length[curr]
        d = 1 if f <= la else -1
        s1 = ln * (ln - 1) // 2
        s2 = ln * (ln - 1) * (2 * ln - 1) // 6
        term = pos * f * ln + (pos * d + f) * s1 + d * s2
        ans = (ans + term) % mod
        pos += ln
        curr = right[curr]

    return ans


if __name__ == "__main__":
    print(solve())
