# Problem 145: https://projecteuler.net/problem=145


def solve():
    total = 0

    for digits in range(1, 10):
        if digits % 2 == 0:
            total += 20 * 30 ** (digits // 2 - 1)
        elif digits % 4 == 3:
            total += 100 * 500 ** ((digits - 3) // 4)

    return total


if __name__ == "__main__":
    print(solve())
