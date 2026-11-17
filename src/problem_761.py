# Problem 761: https://projecteuler.net/problem=761
from math import hypot, pi, sqrt, tan


def solve():
    sides = 6
    turn = 2 * pi / sides
    side = 2 * tan(turn / 2)
    arc = (sides / 2 + 1) * side
    discriminant = arc**2 + 4 * (arc / tan(turn) - 1)
    slope = (arc + sqrt(discriminant)) / 2
    return f"{hypot(1, slope):.8f}"


if __name__ == "__main__":
    print(solve())
