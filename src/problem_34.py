# Problem 34: https://projecteuler.net/problem=34
from math import factorial

def solve():
    facts = [factorial(n) for n in range(10)]
    lim = 7 * facts[9]
    total = 0

    for n in range(10, lim + 1):
        if n == sum(facts[int(d)] for d in str(n)):
            total += n

    return total

if __name__ == "__main__":
    print(solve())