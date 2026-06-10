# Problem 301: https://projecteuler.net/problem=301

BITS = 30


def solve():
    zero, one = 1, 0

    for _ in range(BITS):
        zero, one = zero + one, zero

    return zero + one


if __name__ == "__main__":
    print(solve())
