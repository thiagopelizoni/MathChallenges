# Problem 42: https://projecteuler.net/problem=42
from math import isqrt
from urllib.request import urlopen

URL = "https://projecteuler.net/resources/documents/0042_words.txt"

def fetch_words():
    with urlopen(URL) as f:
        return f.read().decode().replace('"', '').split(',')

def is_triangle(n):
    x = 8 * n + 1
    r = isqrt(x)
    return r * r == x

def solve():
    total = 0

    for word in fetch_words():
        score = sum(ord(c) - 64 for c in word)
        total += is_triangle(score)

    return total

if __name__ == "__main__":
    print(solve())
