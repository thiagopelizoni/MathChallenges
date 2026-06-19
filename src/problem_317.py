# Problem 317: https://projecteuler.net/problem=317

from math import pi


H = 100
V = 20
G = 9.81


def solve():
    a = H + V * V / (2 * G)
    return f"{pi * V * V * a * a / G:.4f}"


if __name__ == "__main__":
    print(solve())
