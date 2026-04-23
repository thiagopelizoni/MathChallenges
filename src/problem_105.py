# Problem 105: https://projecteuler.net/problem=105

from urllib.request import urlopen


DATA_URL = "https://projecteuler.net/resources/documents/0105_sets.txt"


def special(a):
    a = sorted(a)

    for k in range(2, len(a) + 1):
        if sum(a[:k]) <= sum(a[-k + 1 :]):
            return False

    sums = {0}
    for x in a:
        more = {s + x for s in sums}
        if sums & more:
            return False
        sums |= more

    return True


def solve():
    with urlopen(DATA_URL) as res:
        rows = res.read().decode().splitlines()

    return sum(
        sum(a)
        for a in ([int(x) for x in row.split(",")] for row in rows)
        if special(a)
    )


if __name__ == "__main__":
    print(solve())
