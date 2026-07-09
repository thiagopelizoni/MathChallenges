# Problem 376: https://projecteuler.net/problem=376

from math import comb


FACES = 6
WIN = 19


def solve(n=30):
    groups = {
        (a, b, c): [
            (da, db, dc)
            for da in range(FACES - a + 1)
            for db in range(FACES - b + 1)
            for dc in range(FACES - c + 1)
            if da + db + dc
        ]
        for a in range(FACES + 1)
        for b in range(FACES + 1)
        for c in range(FACES + 1)
    }
    states = {(0, 0, 0, 0, 0, 0): 1}
    total = 0

    for levels in range(1, min(3 * FACES, n) + 1):
        nxt = {}
        for (a, b, c, ab, bc, ca), ways in states.items():
            for da, db, dc in groups[a, b, c]:
                state = (
                    a + da,
                    b + db,
                    c + dc,
                    min(WIN, ab + da * b),
                    min(WIN, bc + db * c),
                    min(WIN, ca + dc * a),
                )
                nxt[state] = nxt.get(state, 0) + ways
        states = nxt
        total += comb(n, levels) * states.get((6, 6, 6, WIN, WIN, WIN), 0)

    return total // 3


if __name__ == "__main__":
    print(solve())
