# Problem 36: https://projecteuler.net/problem=36
def is_palindrome(s):
    return s == s[::-1]


def solve():
    total = 0

    for n in range(1, 1000):
        s = str(n)

        a = int(s + s[-2::-1])
        if is_palindrome(bin(a)[2:]):
            total += a

        b = int(s + s[::-1])
        if is_palindrome(bin(b)[2:]):
            total += b

    return total


if __name__ == "__main__":
    print(solve())