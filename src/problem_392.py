# Problem 392: https://projecteuler.net/problem=392
from math import sqrt


# By the x/y and origin symmetries of the objective and constraints, an optimal
# grid uses the same set of positive positions t_1 .. t_P (P = N/2) on both
# axes, mirrored about each axis. For a column with left edge t_k the tightest
# covering height is sqrt(1 - t_k**2); choosing the grid closed under
# t -> sqrt(1 - t**2) lets that height be an actual gridline (no rounding waste),
# so the first-quadrant red area is F = sum (t_{k+1} - t_k) * sqrt(1 - t_k**2)
# and the total red area is 4F. Setting dF/dt_p = 0 yields the recursion
#   t_{p+1} = t_p + sqrt(1-t_p**2) * (sqrt(1-t_{p-1}**2) - sqrt(1-t_p**2)) / t_p
# starting from t_0 = 0, so the whole grid follows from t_1. A shooting method
# picks t_1 so that t_{P+1} = 1.
def build_grid(t1, positive_lines):
    t = [0.0, t1]
    for p in range(1, positive_lines + 1):
        tp, tpm = t[p], t[p - 1]
        if tp >= 1.0:
            return None
        sp, spm = sqrt(1 - tp * tp), sqrt(1 - tpm * tpm)
        t.append(tp + sp * (spm - sp) / tp)
    return t


def endpoint_error(t1, positive_lines):
    grid = build_grid(t1, positive_lines)
    return 1.0 if grid is None else grid[positive_lines + 1] - 1.0


def minimal_red_area(n):
    positive_lines = n // 2
    lo, hi = 1e-9, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if endpoint_error(mid, positive_lines) < 0:
            lo = mid
        else:
            hi = mid
    grid = build_grid((lo + hi) / 2, positive_lines)
    quadrant = sum(
        (grid[k + 1] - grid[k]) * sqrt(1 - grid[k] * grid[k])
        for k in range(positive_lines + 1)
    )
    return 4 * quadrant


def solve():
    return f"{minimal_red_area(400):.10f}"


if __name__ == "__main__":
    print(solve())
