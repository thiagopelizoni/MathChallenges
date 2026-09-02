# Problem 582: https://projecteuler.net/problem=582

from sympy.solvers.diophantine.diophantine import diop_DN


def solve():
    D = 3
    max_diff = 100
    limit = 10**100
    unit_u, unit_x = map(int, diop_DN(D, 1)[0])
    triangles = set()

    for d in range(1, max_diff + 1):
        for u0, x0 in diop_DN(D, d * d):
            for sign in (-1, 1):
                u = abs(int(u0))
                x = sign * abs(int(x0))
                while x < 0 or u <= 2 * limit:
                    if x > d and u % 2 == 0 and x % 2 == d % 2:
                        triangles.add((d, x, u))
                    u, x = unit_u * u + D * unit_x * x, unit_x * u + unit_u * x

    return len(triangles)


if __name__ == "__main__":
    print(solve())
