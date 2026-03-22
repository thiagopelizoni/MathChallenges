# Problem 40: https://projecteuler.net/problem=40
def digit(n):
    width = 1
    start = 1
    count = 9

    while n > width * count:
        n -= width * count
        width += 1
        start *= 10
        count *= 10

    x = start + (n - 1) // width
    i = (n - 1) % width
    return int(str(x)[i])

def solve():
    ans = 1

    for n in (1, 10, 100, 1000, 10000, 100000, 1000000):
        ans *= digit(n)

    return ans

if __name__ == "__main__":
    print(solve())