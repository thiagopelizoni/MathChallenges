# Problem 669: https://projecteuler.net/problem=669
from sympy import fibonacci


def prefix_A(n):
    length = {"A": [1], "C": [1]}
    count = {"A": [1], "C": [0]}
    while length["A"][-1] < n:
        la, lc = length["A"][-1], length["C"][-1]
        ca, cc = count["A"][-1], count["C"][-1]
        length["A"].append(3 * la + 2 * lc)
        length["C"].append(2 * la + lc)
        count["A"].append(3 * ca + 2 * cc)
        count["C"].append(2 * ca + cc)

    image = {"A": "AACAC", "C": "AAC"}

    def take(letter, level, need):
        if need == 0:
            return 0
        if level == 0:
            return 1 if letter == "A" else 0
        got = 0
        for ch in image[letter]:
            span = length[ch][level - 1]
            if need >= span:
                got += count[ch][level - 1]
                need -= span
            else:
                got += take(ch, level - 1, need)
                break
        return got

    return take("A", len(length["A"]) - 1, n)


def solve():
    n = 99194853094755497
    k = 1
    while fibonacci(k) < n:
        k += 1
    seat = 10**16
    m = seat // 2 - 1
    a = prefix_A(m)
    return (a + 1) * fibonacci(k) - m * fibonacci(k - 1) - fibonacci(k + 1) // 2


if __name__ == "__main__":
    print(solve())
