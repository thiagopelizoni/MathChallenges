# Problem 505: https://projecteuler.net/problem=505

MOD = 2**60
LEAF = 1_734_993_956_435


def x(k):
    path = []
    while k > 1:
        path.append(k % 2)
        k //= 2

    value, parent = 1, 0
    for direction in reversed(path):
        if direction:
            child = (2 * value + 3 * parent) % MOD
        else:
            child = (3 * value + 2 * parent) % MOD
        parent, value = value, child
    return value


def solve():
    return x(LEAF)


if __name__ == "__main__":
    print(solve())
