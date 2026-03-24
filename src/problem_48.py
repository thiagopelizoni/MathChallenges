# Problem 48: https://projecteuler.net/problem=48
def solve():
    mod = 10**10
    return sum(pow(n, n, mod) for n in range(1, 1001)) % mod

if __name__ == "__main__":
    print(solve())