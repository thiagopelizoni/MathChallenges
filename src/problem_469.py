# Problem 469: https://projecteuler.net/problem=469

from mpmath import mp


DECIMALS = 14


def solve():
    with mp.workdps(DECIMALS + 20):
        scale = 10**DECIMALS
        rounded = int(mp.nint(scale * (1 + mp.exp(-2)) / 2))
    return f"{rounded // scale}.{rounded % scale:0{DECIMALS}d}"


if __name__ == "__main__":
    print(solve())
