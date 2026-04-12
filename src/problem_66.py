# Problem 66: https://projecteuler.net/problem=66
import math

def solve():
    max_x = 0
    best_d = 0

    for d in range(2, 1001):
        limit = math.isqrt(d)
        if limit * limit == d:
            continue

        m = 0
        den = 1
        a = limit

        h2, h1 = 0, 1
        k2, k1 = 1, 0

        while True:
            h = a * h1 + h2
            k = a * k1 + k2

            if h * h - d * k * k == 1:
                if h > max_x:
                    max_x = h
                    best_d = d
                break

            m = den * a - m
            den = (d - m * m) // den
            a = (limit + m) // den

            h2, h1 = h1, h
            k2, k1 = k1, k

    return best_d

if __name__ == "__main__":
    print(solve())
