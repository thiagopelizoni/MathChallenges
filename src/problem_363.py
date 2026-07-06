# Problem 363: https://projecteuler.net/problem=363

import mpmath as mp


mp.mp.dps = 50


def x_derivative(t, v):
    return 6 * (v - 1) * t + 3 * (2 - 3 * v) * t**2


def y(t, v):
    u = 1 - t
    return 3 * u**2 * t * v + 3 * u * t**2 + t**3


def y_derivative(t, v):
    return 3 * v + 2 * (3 - 6 * v) * t + 3 * (3 * v - 2) * t**2


def enclosed_area(v):
    return mp.quad(lambda t: y(t, v) * -x_derivative(t, v), [0, 1])


def curve_length(v):
    return mp.quad(
        lambda t: mp.sqrt(x_derivative(t, v) ** 2 + y_derivative(t, v) ** 2),
        [0, 1],
    )


def solve():
    v = mp.findroot(lambda a: enclosed_area(a) - mp.pi / 4, (mp.mpf("0.5"), mp.mpf("0.6")))
    quarter_circle = mp.pi / 2
    percentage = 100 * (curve_length(v) - quarter_circle) / quarter_circle
    return f"{float(percentage):.10f}"


if __name__ == "__main__":
    print(solve())
