# Problem 69: https://projecteuler.net/problem=69

def solve():
    limit = 1_000_000
    n = 1
    p = 2
    while n * p <= limit:
        n *= p
        p += 1
        while any(p % i == 0 for i in range(2, int(p**0.5) + 1)):
            p += 1
    return n

if __name__ == "__main__":
    print(solve())
