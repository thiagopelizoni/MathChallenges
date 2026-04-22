# Problem 101: https://projecteuler.net/problem=101

def u(n):
    return sum((-n) ** k for k in range(11))


def fit(seq):
    row = seq[:]
    total = row[-1]

    while len(row) > 1:
        row = [b - a for a, b in zip(row, row[1:])]
        total += row[-1]

    return total


def solve():
    return sum(fit([u(n) for n in range(1, k + 1)]) for k in range(1, 11))


if __name__ == "__main__":
    print(solve())
