# Problem 28: https://projecteuler.net/problem=28
def solve():
    total = 1

    for s in range(3, 1002, 2):
        total += 4 * s * s - 6 * (s - 1)

    return total

if __name__ == "__main__":
    print(solve())