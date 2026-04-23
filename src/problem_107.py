# Problem 107: https://projecteuler.net/problem=107

from urllib.request import urlopen


DATA_URL = "https://projecteuler.net/resources/documents/0107_network.txt"


def solve():
    with urlopen(DATA_URL) as res:
        rows = [line.decode().strip().split(",") for line in res]

    edges = []
    total = 0
    n = len(rows)

    for i in range(n):
        for j in range(i + 1, n):
            if rows[i][j] != "-":
                w = int(rows[i][j])
                total += w
                edges.append((w, i, j))

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    mst = 0
    for w, u, v in sorted(edges):
        ru = find(u)
        rv = find(v)
        if ru != rv:
            parent[ru] = rv
            mst += w

    return total - mst


if __name__ == "__main__":
    print(solve())
