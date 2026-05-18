# Problem 230: https://projecteuler.net/problem=230
A = (
    "14159265358979323846264338327950288419716939937510"
    "58209749445923078164062862089986280348253421170679"
)
B = (
    "82148086513282306647093844609550582231725359408128"
    "48111745028410270193852110555964462294895493038196"
)


def digit(n):
    lens = [len(A), len(B)]
    while lens[-1] < n:
        lens.append(lens[-2] + lens[-1])

    k = len(lens) - 1
    while k > 1:
        left = lens[k - 2]
        if n <= left:
            k -= 2
        else:
            n -= left
            k -= 1

    return (A if k == 0 else B)[n - 1]


def solve():
    return sum(10**n * int(digit((127 + 19 * n) * 7**n)) for n in range(18))


if __name__ == "__main__":
    print(solve())
