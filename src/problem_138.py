# Problem 138: https://projecteuler.net/problem=138


def solve():
    a, b = 17, 305
    total = a + b

    for _ in range(10):
        a, b = b, 18 * b - a
        total += b

    return total


if __name__ == "__main__":
    print(solve())
