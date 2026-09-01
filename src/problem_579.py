# Problem 579: https://projecteuler.net/problem=579
from itertools import permutations, product
from math import gcd, isqrt


def quaternion_units():
    units = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    for i in range(4):
        for j in range(i + 1, 4):
            for sign in (-1, 1):
                unit = [0, 0, 0, 0]
                unit[i] = 1
                unit[j] = sign
                units.append(tuple(unit))
    for signs in product((-1, 1), repeat=3):
        units.append((1, *signs))
    return units


def cube_rotations():
    rotations = []
    for order in permutations(range(3)):
        inversions = sum(order[i] > order[j] for i in range(3) for j in range(i + 1, 3))
        parity = -1 if inversions % 2 else 1
        for signs in product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] == 1:
                rotations.append((order, signs))
    return rotations


CUBE_UNITS = quaternion_units()
CUBE_ROTATIONS = cube_rotations()


def multiply(q, h):
    a, b, c, d = q
    e, f, g, z = h
    return (
        a * e - b * f - c * g - d * z,
        a * f + b * e + c * z - d * g,
        a * g - b * z + c * e + d * f,
        a * z + b * g - c * f + d * e,
    )


def primitive(q):
    common = gcd(*q)
    q = tuple(value // common for value in q)
    first = next(value for value in q if value)
    return tuple(-value for value in q) if first < 0 else q


def rotation_matrix(q):
    a, b, c, d = q
    matrix = (
        a * a + b * b - c * c - d * d,
        2 * (b * c - a * d),
        2 * (b * d + a * c),
        2 * (b * c + a * d),
        a * a - b * b + c * c - d * d,
        2 * (c * d - a * b),
        2 * (b * d - a * c),
        2 * (c * d + a * b),
        a * a - b * b - c * c + d * d,
    )
    common = gcd(*matrix)
    return tuple(value // common for value in matrix)


def right_canonical(q):
    best_num = q[0] * q[0]
    best_den = sum(value * value for value in q)
    original = rotation_matrix(q)
    best_matrix = original

    for unit in CUBE_UNITS[1:]:
        candidate = primitive(multiply(q, unit))
        numerator = candidate[0] * candidate[0]
        denominator = sum(value * value for value in candidate)
        matrix = rotation_matrix(candidate)
        comparison = numerator * best_den - best_num * denominator
        if comparison > 0 or comparison == 0 and matrix > best_matrix:
            best_num = numerator
            best_den = denominator
            best_matrix = matrix

    return original == best_matrix


def orbit_weight(a, x, y, z):
    vectors = set()
    source = (x, y, z)
    for order, signs in CUBE_ROTATIONS:
        vectors.add(tuple(signs[i] * source[order[i]] for i in range(3)))
    if a != x + y + abs(z):
        return len(vectors)
    return sum(right_canonical((a, *vector)) for vector in vectors)


def cube_points(n, q, modulus):
    matrix = rotation_matrix(q)
    side = isqrt(sum(matrix[j] * matrix[j] for j in range(3)))
    widths = [sum(abs(matrix[3 * i + j]) for j in range(3)) for i in range(3)]
    span = max(widths)
    if span > n:
        return 0

    edge_gcds = 0
    for j in range(3):
        edge_gcds += gcd(abs(matrix[j]), abs(matrix[3 + j]), abs(matrix[6 + j]))

    total = 0
    for scale in range(1, n // span + 1):
        placements = 1
        for width in widths:
            placements *= n - scale * width + 1
        r = scale * side
        lattice_points = r**3 + (r + 1) * scale * edge_gcds + 1
        total = (total + placements * lattice_points) % modulus
    return total


def solve():
    n = 5000
    modulus = 10**9
    total = 0

    for a in range(1, isqrt(4 * n) + 1):
        for x in range(a, -1, -1):
            if 2 * a * a < (a + x) ** 2:
                continue
            for y in range(x, -1, -1):
                remaining = 4 * n - a * a - x * x - y * y
                if remaining < 0:
                    continue
                max_z = min(y, a - x - y, isqrt(remaining))
                for z in range(max_z, -1, -1):
                    if gcd(a, x, y, z) != 1:
                        continue

                    signs = (1, -1) if x > y > z > 0 else (1,)
                    for sign in signs:
                        q = (a, x, y, sign * z)
                        weight = orbit_weight(a, x, y, sign * z)
                        total = (total + weight * cube_points(n, q, modulus)) % modulus

    return total


if __name__ == "__main__":
    print(solve())
