# Problem 9: https://projecteuler.net/problem=9
def solve():
    s = 1000

    for a in range(1, s // 3):
        num = s * (s - 2 * a)
        den = 2 * (s - a)
        if num % den == 0:
            b = num // den
            c = s - a - b
            if a < b < c and a * a + b * b == c * c:
                return a * b * c

if __name__ == "__main__":
    print(solve())