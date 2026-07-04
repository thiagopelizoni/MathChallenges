# Problem 360: https://projecteuler.net/problem=360

from collections import Counter
from itertools import permutations, product

from sympy import Matrix


POWER = 10
EVEN_SCALE = 2**POWER
PERMS = tuple(permutations(range(3)))
GENERATOR_MATRICES = (
    Matrix(((5, 0, 0), (0, -3, -4), (0, 4, -3))),
    Matrix(((5, 0, 0), (0, -3, 4), (0, -4, -3))),
    Matrix(((-3, 0, 4), (0, 5, 0), (-4, 0, -3))),
    Matrix(((-3, 0, -4), (0, 5, 0), (4, 0, -3))),
    Matrix(((-3, -4, 0), (4, -3, 0), (0, 0, 5))),
    Matrix(((-3, 4, 0), (-4, -3, 0), (0, 0, 5))),
)
INVERSE_GENERATOR = (1, 0, 3, 2, 5, 4)


def signed_perm_matrix(perm, signs):
    return Matrix(
        tuple(
            tuple(signs[i] if perm[i] == j else 0 for j in range(3))
            for i in range(3)
        )
    )


def label_maps():
    maps = {}
    for perm in PERMS:
        for signs in product((-1, 1), repeat=3):
            g = signed_perm_matrix(perm, signs)
            labels = []
            for m in GENERATOR_MATRICES:
                gm = g * m
                labels.append(
                    next(
                        j
                        for j, n in enumerate(GENERATOR_MATRICES)
                        if gm == n * g
                    )
                )
            maps[(perm, signs)] = tuple(labels)
    return maps


LABEL_MAPS = label_maps()


def transform(label, point):
    x, y, z = point
    if label == 0:
        return 5 * x, -3 * y - 4 * z, 4 * y - 3 * z
    if label == 1:
        return 5 * x, -3 * y + 4 * z, -4 * y - 3 * z
    if label == 2:
        return -3 * x + 4 * z, 5 * y, -4 * x - 3 * z
    if label == 3:
        return -3 * x - 4 * z, 5 * y, 4 * x - 3 * z
    if label == 4:
        return -3 * x - 4 * y, 4 * x - 3 * y, 5 * z
    return -3 * x + 4 * y, -4 * x - 3 * y, 5 * z


def canonical(point, label):
    target = tuple(sorted((abs(point[0]), abs(point[1]), abs(point[2]))))
    best = len(GENERATOR_MATRICES)

    for perm in PERMS:
        moved = tuple(abs(point[i]) for i in perm)
        if moved != target:
            continue

        choices = []
        for i in perm:
            if point[i] > 0:
                choices.append((1,))
            elif point[i] < 0:
                choices.append((-1,))
            else:
                choices.append((-1, 1))

        for signs in product(*choices):
            mapped = LABEL_MAPS[(perm, signs)][label]
            if mapped < best:
                best = mapped

    return target, best


def initial_states():
    states = Counter()
    for point, forbidden in (
        ((1, 0, 0), 1),
        ((-1, 0, 0), 0),
        ((0, 1, 0), 3),
        ((0, -1, 0), 2),
        ((0, 0, 1), 5),
        ((0, 0, -1), 4),
    ):
        states[canonical(point, forbidden)] += 1
    return states


def next_states(states):
    out = Counter()
    for (point, forbidden), count in states.items():
        for label in range(len(GENERATOR_MATRICES)):
            if label == forbidden:
                continue
            child = transform(label, point)
            child_forbidden = INVERSE_GENERATOR[label]
            out[canonical(child, child_forbidden)] += count
    return out


def sphere_sum_for_5_power(power):
    states = initial_states()
    for _ in range(power):
        states = next_states(states)
    return sum(count * sum(point) for (point, _), count in states.items())


def solve():
    return EVEN_SCALE * sphere_sum_for_5_power(POWER)


if __name__ == "__main__":
    print(solve())
