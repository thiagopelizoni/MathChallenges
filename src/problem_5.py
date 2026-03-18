# Problem 5: https://projecteuler.net/problem=5
from math import lcm


def solve():
    ans = 1
    for n in range(2, 21):
        ans = lcm(ans, n)
    return ans


if __name__ == "__main__":
    print(solve())