# Problem 472: https://projecteuler.net/problem=472

from collections import namedtuple


Segment = namedtuple("Segment", "lo hi slope intercept")
Piece = namedtuple("Piece", "lo hi slope intercept count_slope count_intercept")


def seat_segments(limit):
    segments = [Segment(0, min(1, limit), 0, 0)]
    q = 1
    while 2 * q <= limit:
        segments.append(Segment(2 * q, min(3 * q - 1, limit), 0, q))
        if 3 * q <= limit:
            segments.append(Segment(3 * q, min(4 * q - 1, limit), 1, -2 * q))
        q *= 2
    return segments


def candidate(a, b, m):
    lo = max(a.lo, m - b.hi)
    hi = min(a.hi, m - b.lo)
    delta = a.slope - b.slope
    x = hi if delta > 0 else lo
    value = a.slope * x + a.intercept
    value += b.slope * (m - x) + b.intercept
    count = hi - lo + 1 if delta == 0 else 1
    return value, count


def candidate_pieces(limit):
    pieces = []
    segments = seat_segments(limit)

    for a in segments:
        for b in segments:
            lo = a.lo + b.lo
            hi = min(limit, a.hi + b.hi)
            if lo > hi:
                continue

            cuts = {lo, hi + 1}
            for cut in (a.lo + b.hi + 1, a.hi + b.lo + 1):
                if lo < cut <= hi:
                    cuts.add(cut)
            cuts = sorted(cuts)

            for left, right in zip(cuts, cuts[1:]):
                right -= 1
                value, count = candidate(a, b, left)
                if left < right:
                    next_value, next_count = candidate(a, b, left + 1)
                    slope = next_value - value
                    count_slope = next_count - count
                else:
                    slope = count_slope = 0
                pieces.append(
                    Piece(
                        left,
                        right,
                        slope,
                        value - slope * left,
                        count_slope,
                        count - count_slope * left,
                    )
                )
    return pieces


def affine_sum(slope, intercept, lo, hi):
    if lo > hi:
        return 0
    length = hi - lo + 1
    return slope * (lo + hi) * length // 2 + intercept * length


def sum_f(n):
    pieces = candidate_pieces(n - 1)
    cuts = sorted({x for piece in pieces for x in (piece.lo, piece.hi + 1)})
    total = 0

    for lo, end in zip(cuts, cuts[1:]):
        hi = end - 1
        active = [piece for piece in pieces if piece.lo <= lo and piece.hi >= hi]
        groups = {}

        for slope in (0, 1):
            same = [piece for piece in active if piece.slope == slope]
            if not same:
                continue
            intercept = max(piece.intercept for piece in same)
            winners = [piece for piece in same if piece.intercept == intercept]
            groups[slope] = (
                intercept,
                sum(piece.count_slope for piece in winners),
                sum(piece.count_intercept for piece in winners),
            )

        if len(groups) == 1:
            _, slope, intercept = next(iter(groups.values()))
            total += affine_sum(slope, intercept, lo, hi)
            continue

        b0, c0, d0 = groups[0]
        b1, c1, d1 = groups[1]
        tie = b0 - b1
        total += affine_sum(c0, d0, lo, min(hi, tie - 1))
        if lo <= tie <= hi:
            total += c0 * tie + d0 + c1 * tie + d1
        total += affine_sum(c1, d1, max(lo, tie + 1), hi)

    return total


def solve():
    return sum_f(10**12) % 100_000_000


if __name__ == "__main__":
    print(solve())
