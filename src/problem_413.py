# Problem 413: https://projecteuler.net/problem=413


def add_state(states, state, zero, one):
    if zero == 0 and one == 0:
        return
    value = states.get(state)
    if value is None:
        states[state] = [zero, one]
    else:
        value[0] += zero
        value[1] += one


def count_one_child(d):
    dp = {(): [1, 0]}

    for pos in range(d):
        nxt = {}
        digits = range(1, 10) if pos == 0 else range(10)

        for hist, (zero, one) in dp.items():
            base = [0] * d
            for residue, count in enumerate(hist):
                base[10 * residue % d] += count

            for digit in digits:
                shift = digit % d
                counts = base[-shift:] + base[:-shift] if shift else base
                added = counts[0] + (shift == 0)
                if added > 1:
                    continue

                counts = list(counts)
                counts[shift] += 1
                state = tuple(counts)
                if added == 0:
                    add_state(nxt, state, zero, one)
                else:
                    add_state(nxt, state, 0, zero)
        dp = nxt

    return sum(one for zero, one in dp.values())


def count_one_child_eighteen():
    seen = [0] * 9
    seen[0] = 1
    dp = {tuple(seen): [1, 0]}

    for pos in range(18):
        nxt = {}
        digits = range(1, 10) if pos == 0 else range(10)

        for seen, (zero, one) in dp.items():
            for digit in digits:
                shift = digit % 9
                counts = seen[shift:] + seen[:shift]
                added = counts[0] if digit % 2 == 0 else 0
                if added > 1:
                    continue

                state = (counts[0] + 1,) + counts[1:]
                if added == 0:
                    add_state(nxt, state, zero, one)
                else:
                    add_state(nxt, state, 0, zero)
        dp = nxt

    return sum(one for zero, one in dp.values())


def solve():
    return sum(count_one_child(d) for d in range(1, 18)) + \
        count_one_child_eighteen() + count_one_child(19)


if __name__ == "__main__":
    print(solve())
