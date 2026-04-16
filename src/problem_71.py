# Problem 71: https://projecteuler.net/problem=71

def solve():
    lim = 1000000
    d = lim - (lim - 5) % 7
    return (3 * d - 1) // 7

if __name__ == "__main__":
    print(solve())
