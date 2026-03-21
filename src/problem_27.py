# Problem 27: https://projecteuler.net/problem=27
from gmpy2 import is_prime

def run(a, b):
    n = 0
    while is_prime(n * n + a * n + b):
        n += 1
    return n

def solve():
    best = 0
    ans = 0
    bs = [b for b in range(2, 1001) if is_prime(b)]

    for a in range(-999, 1000):
        for b in bs:
            if not is_prime(a + b + 1):
                continue

            cur = run(a, b)
            if cur > best:
                best = cur
                ans = a * b

    return ans

if __name__ == "__main__":
    print(solve())