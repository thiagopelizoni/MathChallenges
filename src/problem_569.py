# Problem 569: https://projecteuler.net/problem=569
from array import array

from sympy import sieve


def solve():
    n = 2_500_000
    sieve.extend_to_no(2 * n)
    primes = sieve[1 : 2 * n + 1]

    x = array("Q", [0])
    y = array("Q", [0])
    for i in range(n - 1):
        p = primes[2 * i + 2]
        x.append(x[-1] + p)
        y.append(y[-1] + p - primes[2 * i + 1])

    offsets = array("Q", [0, 0])
    visible = array("I")
    for k in range(1, n):
        j = k - 1
        visible.append(j)
        best_num = y[k] - y[j]
        best_den = x[k] - x[j]

        while j:
            found = -1
            for pos in range(offsets[j], offsets[j + 1]):
                i = visible[pos]
                num = y[k] - y[i]
                den = x[k] - x[i]
                if num * best_den < best_num * den:
                    found = i
                    best_num, best_den = num, den
                    visible.append(i)
                    break
            if found < 0:
                break
            j = found

        offsets.append(len(visible))

    return len(visible)


if __name__ == "__main__":
    print(solve())
