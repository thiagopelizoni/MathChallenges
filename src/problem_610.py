# Problem 610: https://projecteuler.net/problem=610

from fractions import Fraction
from itertools import product


def solve():
    letter = Fraction(14, 100)
    stop = Fraction(2, 100)
    digits = []
    for one, five, ten in ("CDM", "XLC", "IVX"):
        forms = [one * k for k in range(4)]
        forms.append(one + five)
        forms.extend(five + one * k for k in range(4))
        forms.append(one + ten)
        digits.append(forms)

    values = {"".join(parts): n for n, parts in enumerate(product(*digits))}
    expected = {}
    for roman in sorted(values, key=len, reverse=True):
        children = [roman + c for c in "IVXLCDM" if roman + c in values]
        total = stop * values[roman]
        total += letter * sum(expected[child] for child in children)
        expected[roman] = total / (stop + letter * len(children))

    total = expected[""] + 1000 * letter / (1 - letter)
    return f"{float(total):.8f}"


if __name__ == "__main__":
    print(solve())
