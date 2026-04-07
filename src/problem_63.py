# Problem 63: https://projecteuler.net/problem=63

def solve():
    ans = 0
    for b in range(1, 10):
        n = 1
        while 10**(n - 1) <= b**n:
            ans += 1
            n += 1
    return ans

if __name__ == "__main__":
    print(solve())
