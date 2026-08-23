# Problem 561: https://projecteuler.net/problem=561


def solve():
    m = 904_961
    n = 10 ** 12
    total = 0
    power = 4
    while power <= n + 1:
        total += n // power + m * ((n + 1) // power)
        power *= 2
    return total


if __name__ == "__main__":
    print(solve())
