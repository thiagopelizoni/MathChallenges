# Problem 84: https://projecteuler.net/problem=84

def next_r(pos):
    for r in (5, 15, 25, 35):
        if r > pos:
            return r
    return 5


def next_u(pos):
    return 12 if pos < 12 or pos >= 28 else 28


def resolve(pos):
    if pos == 30:
        return [(10, 1.0)]

    if pos in (2, 17, 33):
        return [(0, 1 / 16), (10, 1 / 16), (pos, 14 / 16)]

    if pos in (7, 22, 36):
        out = {}

        def add(dst, p):
            out[dst] = out.get(dst, 0.0) + p

        for dst in (0, 10, 11, 24, 39, 5):
            add(dst, 1 / 16)
        add(next_r(pos), 1 / 16)
        add(next_r(pos), 1 / 16)
        add(next_u(pos), 1 / 16)
        for dst, p in resolve(pos - 3):
            add(dst, p / 16)
        add(pos, 6 / 16)
        return list(out.items())

    return [(pos, 1.0)]


def solve():
    rolls = []
    for a in range(1, 5):
        for b in range(1, 5):
            rolls.append((a + b, a == b, 1 / 16))

    def idx(pos, d):
        return pos * 3 + d

    state = [0.0] * 120
    state[idx(0, 0)] = 1.0

    while True:
        nxt = [0.0] * 120
        for pos in range(40):
            for d in range(3):
                cur = state[idx(pos, d)]
                if cur == 0.0:
                    continue

                for step, dbl, p_roll in rolls:
                    p = cur * p_roll
                    if dbl and d == 2:
                        nxt[idx(10, 0)] += p
                        continue

                    nd = d + 1 if dbl else 0
                    land = (pos + step) % 40
                    for dst, p_move in resolve(land):
                        nxt[idx(dst, 0 if dst == 10 else nd)] += p * p_move

        delta = max(abs(a - b) for a, b in zip(state, nxt))
        state = nxt
        if delta < 1e-15:
            break

    p_pos = [sum(state[idx(pos, d)] for d in range(3)) for pos in range(40)]
    top = sorted(range(40), key=lambda pos: (-p_pos[pos], pos))[:3]
    return "".join(f"{pos:02d}" for pos in top)


if __name__ == "__main__":
    print(solve())
