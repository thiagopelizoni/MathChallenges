# Problem 789: https://projecteuler.net/problem=789

from sympy import primerange


def products(primes, budget, start=0, excess=0, product=1):
    yield excess, product
    for i in range(start, len(primes)):
        q = primes[i]
        cost = excess + q - 1
        if cost > budget:
            break
        yield from products(primes, budget, i, cost, product * q)


def solve():
    p = 2_000_000_011
    budget = 1
    while True:
        primes = list(primerange(2, budget + 2))
        complements = {}
        for excess, product in products(primes[1::2], budget):
            residue = -pow(product, -1, p) % p
            if residue not in complements or excess < complements[residue][0]:
                complements[residue] = excess, product

        best = budget + 1
        answer = None
        for excess, product in products(primes[::2], budget):
            match = complements.get(product % p)
            if match is not None and excess + match[0] < best:
                best = excess + match[0]
                answer = product * match[1]
        if answer is not None:
            return answer
        budget *= 2


if __name__ == "__main__":
    print(solve())
