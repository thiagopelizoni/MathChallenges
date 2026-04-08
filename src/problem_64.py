# Problem 64: https://projecteuler.net/problem=64
import math

def solve():
    count = 0
    for n in range(2, 10001):
        limit = math.isqrt(n)
        if limit * limit == n:
            continue
            
        m = 0
        d = 1
        a = limit
        period = 0
        
        while a != 2 * limit:
            m = d * a - m
            d = (n - m * m) // d
            a = (limit + m) // d
            period += 1
            
        if period % 2 == 1:
            count += 1
            
    return count

if __name__ == "__main__":
    print(solve())
