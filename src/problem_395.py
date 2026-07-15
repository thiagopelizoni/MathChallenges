# Problem 395: https://projecteuler.net/problem=395
from heapq import heappop, heappush
from itertools import count


left_scale = complex(16, 12) / 25
children = ((1j, left_scale), (1j + left_scale, complex(9, -12) / 25))
corners = (0j, 1, 1j, 1 + 1j)
radius = 5.0


def support_bounds(direction, tol=1e-13):
    def project(z):
        return (direction.conjugate() * z).real

    best = max(map(project, corners))
    serial = count()
    queue = [(-radius, next(serial), 0j, 1 + 0j)]

    while -queue[0][0] > best + tol:
        _, _, p, v = heappop(queue)
        for offset, scale in children:
            q, w = p + v * offset, v * scale
            best = max(best, max(project(q + w * z) for z in corners))
            upper = project(q) + radius * abs(w)
            if upper > best + tol:
                heappush(queue, (-upper, next(serial), q, w))

    return best, -queue[0][0]


def solve():
    bounds = [support_bounds(d) for d in (1 + 0j, -1 + 0j, 1j, -1j)]
    lower = (bounds[0][0] + bounds[1][0]) * (bounds[2][0] + bounds[3][0])
    upper = (bounds[0][1] + bounds[1][1]) * (bounds[2][1] + bounds[3][1])
    return f"{(lower + upper) / 2:.10f}"


if __name__ == "__main__":
    print(solve())
