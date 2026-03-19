# Problem 16: https://projecteuler.net/problem=16
def solve():
    return sum(map(int, str(2 ** 1000)))

if __name__ == "__main__":
    print(solve())