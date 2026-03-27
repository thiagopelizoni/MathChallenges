# Problem 59: https://projecteuler.net/problem=59
from itertools import product
from string import ascii_lowercase
from urllib.request import urlopen

URL = "https://projecteuler.net/resources/documents/0059_cipher.txt"

def fetch_cipher():
    with urlopen(URL) as f:
        return bytes(map(int, f.read().decode().strip().split(",")))

def solve():
    cipher = fetch_cipher()
    best = 0, b""
    for key in product(map(ord, ascii_lowercase), repeat=3):
        plain = bytes(c ^ key[i % 3] for i, c in enumerate(cipher))
        if any(c < 32 or c > 126 for c in plain):
            continue
        score = sum(plain.count(c) for c in b" etaoinshrdluETAOINSHRDLU")
        if score > best[0]:
            best = score, plain
    return sum(best[1])


if __name__ == "__main__":
    print(solve())
