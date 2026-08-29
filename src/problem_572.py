# Problem 572: https://projecteuler.net/problem=572

from math import factorial, gcd


def class_size(u):
    multiplicities = {}
    for value in u:
        multiplicities[value] = multiplicities.get(value, 0) + 1

    permutations = factorial(3)
    for multiplicity in multiplicities.values():
        permutations //= factorial(multiplicity)

    nonzero = sum(value != 0 for value in u)
    return permutations * 2 ** (nonzero - 1)


def count_dot_one(u, ranges):
    choices = []
    for k, coefficient in enumerate(u):
        if coefficient == 0:
            continue
        others = [j for j in range(3) if j != k]
        work = 1
        for j in others:
            low, high = ranges[j]
            work *= high - low + 1
        choices.append((work, k, others))

    _, k, (i, j) = min(choices)
    coefficient = u[k]
    low, high = ranges[k]
    total = 0

    for vi in range(ranges[i][0], ranges[i][1] + 1):
        partial = 1 - u[i] * vi
        for vj in range(ranges[j][0], ranges[j][1] + 1):
            value = partial - u[j] * vj
            if value % coefficient == 0 and low <= value // coefficient <= high:
                total += 1

    return total


def solve():
    n = 200
    rank_one = 0
    rank_two = 0

    for z in range(1, n + 1):
        limit = n // z
        cube = [(-limit, limit)] * 3

        for y in range(z + 1):
            for x in range(y + 1):
                if gcd(gcd(x, y), z) != 1:
                    continue

                u = (x, y, z)
                weight = class_size(u)
                rank_one += weight * count_dot_one(u, cube)

                ranges = []
                for j, uj in enumerate(u):
                    other_max = max(u[k] for k in range(3) if k != j)
                    low, high = -n, n
                    if other_max:
                        bound = n // other_max
                        low, high = -bound, bound
                    if uj:
                        low = max(low, -((n - 1) // uj))
                        high = min(high, (n + 1) // uj)
                    ranges.append((low, high))

                rank_two += weight * count_dot_one(u, ranges)

    return 2 + rank_one + rank_two


if __name__ == "__main__":
    print(solve())
