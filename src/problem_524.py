# Problem 524: https://projecteuler.net/problem=524

P = (
    *range(1, 25),
    26,
    25,
    27,
    28,
    30,
    32,
    34,
    36,
    38,
    40,
    39,
    42,
    45,
    43,
    41,
    37,
    35,
    33,
    31,
    29,
    44,
)


def solve():
    remaining = list(range(1, len(P) + 1))
    rank = 0
    for value in P:
        rank = rank * len(remaining) + remaining.index(value)
        remaining.remove(value)
    return rank + 1


if __name__ == "__main__":
    print(solve())
