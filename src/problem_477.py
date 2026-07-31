# Problem 477: https://projecteuler.net/problem=477


def fuse(values, stack=None):
    if stack is None:
        stack = []
    for value in values:
        stack.append(value)
        while len(stack) >= 3 and stack[-3] <= stack[-2] >= stack[-1]:
            stack[-3] = stack[-3] - stack[-2] + stack[-1]
            stack.pop()
            stack.pop()
    return stack


def game_score(n):
    mod = 1_000_000_007
    values = []
    seen = {}
    value = 0

    while value not in seen and len(values) < n:
        seen[value] = len(values)
        values.append(value)
        value = (value * value + 45) % mod

    if len(values) == n:
        stack = fuse(values)
        total = sum(values)
    else:
        start = seen[value]
        prefix = values[:start]
        cycle = values[start:]
        copies, remainder = divmod(n - start, len(cycle))
        total = sum(prefix) + copies * sum(cycle) + sum(cycle[:remainder])
        stack = fuse(prefix)
        compact_cycle = fuse(cycle)
        for _ in range(copies):
            fuse(compact_cycle, stack)
        fuse(cycle[:remainder], stack)

    ordered = sorted(stack, reverse=True)
    advantage = sum(ordered[::2]) - sum(ordered[1::2])
    return (total + advantage) // 2


def solve():
    return game_score(10**8)


if __name__ == "__main__":
    print(solve())
