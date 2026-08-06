# Problem 509: https://projecteuler.net/problem=509

MOD = 1_234_567_890
N = 123_456_787_654_321


def grundy_counts(n):
    counts = []
    power = 1
    while power <= n:
        counts.append(n // power - n // (2 * power))
        power *= 2
    return counts


def winning_positions(n):
    counts = grundy_counts(n)
    losing = 0
    for i, left in enumerate(counts):
        for j, right in enumerate(counts):
            third = i ^ j
            if third < len(counts):
                losing += left * right * counts[third]
    return n**3 - losing


def solve():
    return winning_positions(N) % MOD


if __name__ == "__main__":
    print(solve())
