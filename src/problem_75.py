# Problem 75: https://projecteuler.net/problem=75
import math

def solve():
    limit = 1500000
    counts = [0] * (limit + 1)
    m_limit = math.isqrt(limit // 2)

    for m in range(2, m_limit + 1):
        for n in range(1, m):
            if (m + n) % 2 == 1 and math.gcd(m, n) == 1:
                p = 2 * m * (m + n)
                for k in range(p, limit + 1, p):
                    counts[k] += 1

    return sum(1 for c in counts if c == 1)

if __name__ == "__main__":
    print(solve())
