# Problem 346: https://projecteuler.net/problem=346


LIMIT = 10**12


def solve():
    repunits = {1}
    b = 2

    while b * b + b + 1 < LIMIT:
        n = b * b + b + 1
        p = b * b

        while n < LIMIT:
            repunits.add(n)
            p *= b
            n += p

        b += 1

    return sum(repunits)


if __name__ == "__main__":
    print(solve())
