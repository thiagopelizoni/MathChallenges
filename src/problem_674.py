# Problem 674: https://projecteuler.net/problem=674

import urllib.request


def solve():
    url = "https://projecteuler.net/resources/documents/0674_i_expressions.txt"
    text = urllib.request.urlopen(url, timeout=20).read().decode("utf-8")
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    nodes = {}
    left_ch = []
    right_ch = []

    def parse(s):
        stack = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == "I" and i + 1 < n and s[i + 1] == "(":
                stack.append([])
                i += 2
            elif s[i] == ",":
                i += 1
            elif s[i] == ")":
                l, r = stack.pop()
                key = ("I", l, r)
                nid = nodes.get(key)
                if nid is None:
                    nid = len(left_ch)
                    nodes[key] = nid
                    left_ch.append(l)
                    right_ch.append(r)
                if stack:
                    stack[-1].append(nid)
                else:
                    return nid
                i += 1
            else:
                j = i
                while j < n and s[j].isalpha():
                    j += 1
                key = ("V", s[i:j])
                nid = nodes.get(key)
                if nid is None:
                    nid = len(left_ch)
                    nodes[key] = nid
                    left_ch.append(-1)
                    right_ch.append(-1)
                if stack:
                    stack[-1].append(nid)
                else:
                    return nid
                i = j

    roots = [parse(line) for line in lines]
    mod = 10**9

    def least_simultaneous(r1, r2):
        parent = {}

        def find(u):
            while u in parent:
                p = parent[u]
                if p in parent:
                    parent[u] = parent[p]
                u = p
            return u

        queue = [(r1, r2)]
        while queue:
            u, v = queue.pop()
            u = find(u)
            v = find(v)
            if u == v:
                continue
            if left_ch[u] == -1 and left_ch[v] != -1:
                u, v = v, u
            parent[v] = u
            if left_ch[u] != -1 and left_ch[v] != -1:
                queue.append((left_ch[u], left_ch[v]))
                queue.append((right_ch[u], right_ch[v]))

        state = {}
        val = {}
        root = find(r1)
        stack = [(root, 0)]

        while stack:
            u, phase = stack.pop()
            if phase == 0:
                st = state.get(u, 0)
                if st == 1:
                    return 0
                if st == 2:
                    continue
                state[u] = 1
                if left_ch[u] == -1:
                    val[u] = 0
                    state[u] = 2
                else:
                    lu = find(left_ch[u])
                    ru = find(right_ch[u])
                    stack.append((u, 1))
                    stack.append((ru, 0))
                    stack.append((lu, 0))
            else:
                x = val[find(left_ch[u])]
                y = val[find(right_ch[u])]
                val[u] = ((1 + x + y) ** 2 + y - x) % mod
                state[u] = 2

        return val[root]

    ans = 0
    m = len(roots)
    for i in range(m):
        r1 = roots[i]
        for j in range(i + 1, m):
            ans = (ans + least_simultaneous(r1, roots[j])) % mod

    return ans


if __name__ == "__main__":
    print(solve())
