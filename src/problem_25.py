# Problem 25: https://projecteuler.net/problem=25
def solve():
    a, b = 1, 1
    n = 2
    lim = 10**999

    while b < lim:
        a, b = b, a + b
        n += 1

    return n

if __name__ == "__main__":
    print(solve())