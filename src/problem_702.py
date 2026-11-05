# Problem 702: https://projecteuler.net/problem=702


def floor_moments(n, m, a, b=0):
    q, a = divmod(a, m)
    r, b = divmod(b, m)
    s1 = n * (n - 1) // 2
    s2 = n * (n - 1) * (2 * n - 1) // 6
    y = (a * (n - 1) + b) // m
    f = g = h = 0
    if y:
        u, v, w = floor_moments(y, a, m, m - b + a - 1)
        f = n * y - u
        g = y * s1 - (w - u) // 2
        h = n * y * y - 2 * v - u
    return (
        f + q * s1 + r * n,
        g + q * s2 + r * s1,
        h + q * q * s2 + 2 * q * r * s1 + r * r * n + 2 * q * g + 2 * r * f,
    )


def solve(n=123456789):
    triangles = n * (3 * n + 1) // 2
    total = triangles
    d = 2
    while d <= n:
        _, g, _ = floor_moments(d, d, n)
        weighted = n * d * (d - 1) * (2 * d - 1) // 6 - d * g
        reached = 3 * (2 * weighted - d * (d - 1)) // (2 * d)
        total += triangles - reached
        d *= 2
    t = 2 * n - d
    if t >= 0:
        a = pow(d, -1, n)
        f, g, _ = floor_moments(t + 1, n, a)
        residues = a * t * (t + 1) // 2 - n * f
        weighted = a * t * (t + 1) * (2 * t + 1) // 6 - n * g
        carries = ((2 * t + 1) * residues - 3 * weighted) // n
        total += (t + 1) * (t + 2) - carries
    return total


if __name__ == "__main__":
    print(solve())
