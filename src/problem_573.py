# Problem 573: https://projecteuler.net/problem=573
import math


def solve():
    n = 1_000_000
    term = math.exp((n - 1) * math.log1p(-1 / n))
    terms = [term]

    for k in range(1, n // 2):
        m = n - k
        log_ratio = k * math.log1p(1 / k)
        log_ratio += (m - 1) * math.log1p(-1 / m)
        term *= math.exp(log_ratio)
        terms.append(term)

    total = 1 + 2 * math.fsum(terms[:-1]) + terms[-1]
    return f"{total:.4f}"


if __name__ == "__main__":
    print(solve())
