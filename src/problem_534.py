# Problem 534: https://projecteuler.net/problem=534


N = 14
CUTOVER = 9


def count_reach(n, reach):
    if reach == 0:
        return n**n

    half = (n + 1) // 2
    states = {col: 1 if n % 2 and col == n // 2 else 2 for col in range(half)}
    keep = n**reach
    marked = [0] * n
    stamp = 0

    for row in range(1, n):
        nxt = {}
        length = min(row, reach)
        for state, count in states.items():
            stamp += 1
            code = state
            for distance in range(1, length + 1):
                col = code % n
                code //= n
                marked[col] = stamp
                if col >= distance:
                    marked[col - distance] = stamp
                if col + distance < n:
                    marked[col + distance] = stamp
            for col in range(n):
                if marked[col] != stamp:
                    code = state * n + col
                    if row >= reach:
                        code %= keep
                    nxt[code] = nxt.get(code, 0) + count
        states = nxt
    return sum(states.values())


def count_long_reaches(n, reach):
    cols = [False] * n
    down = [False] * (2 * n - 1)
    up = [False] * (2 * n - 1)
    placed = [0] * n

    def visit(row, nearest):
        if row == n:
            return nearest - reach

        total = 0
        for col in range(n):
            a = row - col + n - 1
            b = row + col
            if cols[col] or down[a] or up[b]:
                continue

            new_nearest = nearest
            for distance in range(reach + 1, row + 1):
                old = placed[row - distance]
                if col == old or abs(col - old) == distance:
                    new_nearest = min(new_nearest, distance)
                    break

            placed[row] = col
            cols[col] = down[a] = up[b] = True
            if row >= reach:
                old = placed[row - reach]
                old_a = row - reach - old + n - 1
                old_b = row - reach + old
                cols[old] = down[old_a] = up[old_b] = False

            total += visit(row + 1, new_nearest)

            if row >= reach:
                old = placed[row - reach]
                old_a = row - reach - old + n - 1
                old_b = row - reach + old
                cols[old] = down[old_a] = up[old_b] = True
            cols[col] = down[a] = up[b] = False
        return total

    total = 0
    for col in range((n + 1) // 2):
        placed[0] = col
        cols[col] = down[n - 1 - col] = up[col] = True
        weight = 1 if n % 2 and col == n // 2 else 2
        total += weight * visit(1, n)
        cols[col] = down[n - 1 - col] = up[col] = False
    return total


def weak_queens(n):
    cutover = min(CUTOVER, n - 1)
    return sum(count_reach(n, reach) for reach in range(cutover)) + count_long_reaches(n, cutover)


def solve():
    return weak_queens(N)


if __name__ == "__main__":
    print(solve())
