# Problem 100: https://projecteuler.net/problem=100

def solve():
    b, n = 15, 21

    while n <= 10**12:
        b, n = 3 * b + 2 * n - 2, 4 * b + 3 * n - 3

    return b


if __name__ == "__main__":
    print(solve())
