# Problem 55: https://projecteuler.net/problem=55
def is_lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        s = str(n)
        if s == s[::-1]:
            return False
    return True

def solve():
    return sum(is_lychrel(n) for n in range(1, 10_000))

if __name__ == "__main__":
    print(solve())
