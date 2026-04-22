# Problem 102: https://projecteuler.net/problem=102

from urllib.request import urlopen


DATA_URL = "https://projecteuler.net/resources/documents/0102_triangles.txt"


def contains_origin(row):
    x1, y1, x2, y2, x3, y3 = row
    a = x1 * y2 - y1 * x2
    b = x2 * y3 - y2 * x3
    c = x3 * y1 - y3 * x1

    return a > 0 and b > 0 and c > 0 or a < 0 and b < 0 and c < 0


def solve():
    with urlopen(DATA_URL) as res:
        lines = res.read().decode().splitlines()

    return sum(contains_origin(map(int, line.split(","))) for line in lines)


if __name__ == "__main__":
    print(solve())
