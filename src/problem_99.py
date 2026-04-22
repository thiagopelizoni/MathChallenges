# Problem 99: https://projecteuler.net/problem=99

from math import log
from urllib.request import urlopen


DATA_URL = "https://projecteuler.net/resources/documents/0099_base_exp.txt"


def solve():
    with urlopen(DATA_URL) as res:
        lines = res.read().decode().splitlines()

    return max(
        range(1, len(lines) + 1),
        key=lambda i: int(lines[i - 1].split(",")[1])
        * log(int(lines[i - 1].split(",")[0])),
    )


if __name__ == "__main__":
    print(solve())
