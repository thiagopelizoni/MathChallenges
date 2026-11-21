# Problem 779: https://projecteuler.net/problem=779

from decimal import ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN, Decimal, localcontext

from sympy import sieve


def solve():
    places = 12
    unit = Decimal(f"1e-{places}")
    limit = 10 ** ((places + 1) // 2)

    while True:
        bounds = []
        for rounding in (ROUND_FLOOR, ROUND_CEILING):
            with localcontext() as ctx:
                ctx.prec = places + len(str(limit**2))
                ctx.rounding = rounding
                total = Decimal(0)
                density = Decimal(1)

                for p in sieve.primerange(2, limit + 1):
                    total += density / (p * (p - 1)**2)
                    density = density * (p - 1) / p

                if rounding == ROUND_CEILING:
                    total += density / (2 * limit * (limit - 1))
                bounds.append(total.quantize(unit, rounding=ROUND_HALF_EVEN))

        lower, upper = bounds
        if lower == upper:
            return format(lower, "f")
        limit *= 2


if __name__ == "__main__":
    print(solve())
