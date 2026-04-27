# Problem 137: https://projecteuler.net/problem=137


def solve():
    fib = [0, 1]
    for _ in range(31):
        fib.append(fib[-1] + fib[-2])

    return fib[30] * fib[31]


if __name__ == "__main__":
    print(solve())
