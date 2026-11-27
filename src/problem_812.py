# Problem 812: https://projecteuler.net/problem=812
from operator import mul

from sympy import primerange


def solve(n=10_000):
    mod = 998244353
    primes = list(primerange(3, 2 * n + 2))
    parts = [0] * (n + 1)

    def odd_orders(start, phi):
        for i in range(start, len(primes)):
            p = primes[i]
            totient = phi * (p - 1)
            if totient > 2 * n:
                break
            while totient <= 2 * n:
                degree = totient // 2
                while degree <= n:
                    parts[degree] += 1
                    degree *= 2
                odd_orders(i + 1, totient)
                totient *= p

    odd_orders(0, 1)
    log_derivative = [0] * (n + 1)
    for degree, count in enumerate(parts):
        if count:
            for k in range(degree, n + 1, degree):
                log_derivative[k] += degree * count

    ways = [1]
    for k in range(1, n + 1):
        total = sum(map(mul, ways, log_derivative[k:0:-1]))
        ways.append(total * pow(k, -1, mod) % mod)

    ordinary = ways[n]
    degree = 1
    while degree <= n:
        for k in range(degree, n + 1):
            ways[k] = (ways[k] + ways[k - degree]) % mod
        degree *= 2
    for k in range(1, n + 1):
        ways[k] = (ways[k] + ways[k - 1]) % mod
    return (ordinary + ways[n]) * pow(2, -1, mod) % mod


if __name__ == "__main__":
    print(solve())
