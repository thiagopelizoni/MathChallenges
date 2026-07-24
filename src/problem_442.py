# Problem 442: https://projecteuler.net/problem=442


N = 10**18
DIGITS = 19


def solve():
    forbidden = []
    power = 11
    while len(str(power)) <= DIGITS:
        forbidden.append(str(power))
        power *= 11

    prefixes = {""}
    for word in forbidden:
        prefixes.update(word[:i] for i in range(1, len(word)))
    states = sorted(prefixes, key=lambda state: (len(state), state))
    indexes = {state: i for i, state in enumerate(states)}

    transitions = []
    for state in states:
        row = []
        for digit in map(str, range(10)):
            candidate = state + digit
            if any(candidate.endswith(word) for word in forbidden):
                row.append(-1)
                continue
            suffix = max(
                (prefix for prefix in prefixes if candidate.endswith(prefix)),
                key=len,
            )
            row.append(indexes[suffix])
        transitions.append(row)

    ways = [[1] * len(states)]
    for _ in range(DIGITS):
        previous = ways[-1]
        ways.append(
            [
                sum(previous[next_state] for next_state in row if next_state >= 0)
                for row in transitions
            ]
        )

    rank = N
    state = indexes[""]
    result = []
    for remaining in range(DIGITS - 1, -1, -1):
        for digit, next_state in enumerate(transitions[state]):
            if next_state < 0:
                continue
            count = ways[remaining][next_state]
            if rank >= count:
                rank -= count
            else:
                result.append(str(digit))
                state = next_state
                break
    return int("".join(result))


if __name__ == "__main__":
    print(solve())
