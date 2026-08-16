# Problem 544: https://projecteuler.net/problem=544

from functools import cache


MOD = 1_000_000_007


def grid_polynomial(rows, cols):
    @cache
    def canonical(state):
        labels = {}
        result = []
        for x in state:
            if x < 0:
                result.append(-1)
            else:
                if x not in labels:
                    labels[x] = len(labels)
                result.append(labels[x])
        return tuple(result)

    @cache
    def place(state, pos, label):
        changed = list(state)
        changed[pos] = label
        return canonical(tuple(changed))

    def add(target, poly):
        if len(target) < len(poly):
            target.extend([0] * (len(poly) - len(target)))
        for i, a in enumerate(poly):
            target[i] = (target[i] + a) % MOD

    def add_new(target, poly, used):
        if len(target) <= len(poly):
            target.extend([0] * (len(poly) + 1 - len(target)))
        for i, a in enumerate(poly):
            target[i] = (target[i] - used * a) % MOD
            target[i + 1] = (target[i + 1] + a) % MOD

    dp = {(-1,) * rows: [1]}
    for col in range(cols):
        for row in range(rows):
            next_dp = {}
            for state, poly in dp.items():
                used = max(state) + 1
                up = state[row - 1] if row else -2
                left = state[row] if col else -2

                for label in range(used):
                    if label == up or label == left:
                        continue
                    new_state = place(state, row, label)
                    add(next_dp.setdefault(new_state, []), poly)

                new_state = place(state, row, used)
                add_new(next_dp.setdefault(new_state, []), poly, used)
            dp = next_dp

    result = []
    for poly in dp.values():
        add(result, poly)
    return result


def evaluate(poly, x):
    result = 0
    for a in reversed(poly):
        result = (result * x + a) % MOD
    return result


def extrapolate(values, x):
    differences = values[:]
    choose = 1
    result = 0
    for degree in range(len(values)):
        result = (result + differences[0] * choose) % MOD
        differences = [
            (differences[i + 1] - differences[i]) % MOD
            for i in range(len(differences) - 1)
        ]
        choose *= x - degree
        choose %= MOD
        choose *= pow(degree + 1, -1, MOD)
        choose %= MOD
    return result


def solve():
    poly = grid_polynomial(9, 10)
    values = [0]
    for k in range(1, len(poly) + 1):
        values.append((values[-1] + evaluate(poly, k)) % MOD)
    return extrapolate(values, 1_112_131_415)


if __name__ == "__main__":
    print(solve())
