# Problem 667: https://projecteuler.net/problem=667
import numpy as np
from scipy.optimize import brentq, minimize_scalar


def pentagon(b):
    c, s = np.cos(b), np.sin(b)
    d = np.sqrt(max(0.0, 1 - (c + 0.5) ** 2))
    V = np.array([(-0.5, 0), (0.5, 0), (0.5 + c, s), (0, s - d), (-0.5 - c, s)])
    area = (1 + c) * s - (1 + 2 * c) / 2 * d
    return V, area


def scale(V, phi):
    phi = np.atleast_1d(phi)
    c, s = np.cos(phi)[:, None], np.sin(phi)[:, None]
    x = c * V[:, 0] - s * V[:, 1]
    y = s * V[:, 0] + c * V[:, 1]
    qx = x.max(1)[:, None] - x
    qy = y.max(1)[:, None] - y
    m = np.minimum(qx, qy).max(1)
    for i in range(5):
        j = (i + 1) % 5
        dx, dy = qx[:, j] - qx[:, i], qy[:, j] - qy[:, i]
        with np.errstate(divide="ignore", invalid="ignore"):
            t = (qy[:, i] - qx[:, i]) / (dx - dy)
        m = np.where(np.logical_and(t > 0, t < 1), np.maximum(m, qx[:, i] + t * dx), m)
    return 1 / m


def corner(b):
    V, _ = pentagon(b)
    ph = np.linspace(np.pi / 2, np.pi, 2001)
    sig = scale(V, ph)
    best = np.inf
    for i in range(1, len(ph) - 1):
        if sig[i] <= sig[i - 1] and sig[i] <= sig[i + 1]:
            r = minimize_scalar(lambda f: scale(V, f)[0], bounds=(ph[i - 1], ph[i + 1]),
                                method="bounded", options={"xatol": 1e-14})
            best = min(best, r.fun)
    return best


def solve():
    b = brentq(lambda b: corner(b) - 1 / np.sin(b), np.pi / 3, np.pi / 2, xtol=1e-15)
    _, area = pentagon(b)
    return f"{area / np.sin(b) ** 2:.10f}"


if __name__ == "__main__":
    print(solve())
