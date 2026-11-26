# Problem 807: https://projecteuler.net/problem=807

from scipy.stats import irwinhall


def solve():
    n = 80
    probability = irwinhall.pdf(n, 2 * n)
    return f"{probability:.10f}"


if __name__ == "__main__":
    print(solve())
