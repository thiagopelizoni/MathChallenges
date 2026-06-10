# Problem 303: https://projecteuler.net/problem=303

from collections import deque


N = 10_000


def f(n):
    prev = [-1] * n
    digit = [""] * n
    q = deque()

    for d in (1, 2):
        r = d % n
        if prev[r] == -1:
            prev[r] = -2
            digit[r] = str(d)
            if r == 0:
                return d
            q.append(r)

    while q:
        r = q.popleft()
        for d in (0, 1, 2):
            nr = (10 * r + d) % n
            if prev[nr] != -1:
                continue

            prev[nr] = r
            digit[nr] = str(d)
            if nr == 0:
                s = []
                while nr != -2:
                    s.append(digit[nr])
                    nr = prev[nr]
                return int("".join(reversed(s)))

            q.append(nr)


def solve():
    return sum(f(n) // n for n in range(1, N + 1))


if __name__ == "__main__":
    print(solve())
