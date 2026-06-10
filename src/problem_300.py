# Problem 300: https://projecteuler.net/problem=300

N = 15
STEP = ((1, 0), (-1, 0), (0, 1), (0, -1))


def contact_graphs():
    pair = {}
    for i in range(N):
        for j in range(i + 1, N):
            pair[i, j] = len(pair)

    pos = {(0, 0): 0, (1, 0): 1}
    graphs = set()

    def search(k, x, y, graph):
        if k == N:
            graphs.add(graph)
            return

        for dx, dy in STEP:
            nx, ny = x + dx, y + dy
            if (nx, ny) in pos:
                continue

            ng = graph | (1 << pair[k - 1, k])
            for q in ((nx + 1, ny), (nx - 1, ny), (nx, ny + 1), (nx, ny - 1)):
                i = pos.get(q)
                if i is not None and i < k - 1:
                    ng |= 1 << pair[i, k]

            pos[nx, ny] = k
            search(k + 1, nx, ny, ng)
            del pos[nx, ny]

    search(2, 1, 0, 1 << pair[0, 1])

    maximal = []
    for graph in sorted(graphs, key=int.bit_count, reverse=True):
        if not any(graph & ~other == 0 for other in maximal):
            maximal.append(graph)

    return pair, maximal


def protein_pairs(pair):
    pairs = []
    for protein in range(1 << N):
        mask = 0
        for i in range(N):
            if protein >> i & 1:
                for j in range(i + 1, N):
                    if protein >> j & 1:
                        mask |= 1 << pair[i, j]
        pairs.append(mask)
    return pairs


def solve():
    pair, graphs = contact_graphs()
    total = 0

    for protein in protein_pairs(pair):
        total += max((graph & protein).bit_count() for graph in graphs)

    q, r = divmod(total, 1 << N)
    return f"{q}.{r * 5**N:0{N}d}".rstrip("0")


if __name__ == "__main__":
    print(solve())
