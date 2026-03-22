# Problem 30: https://projecteuler.net/problem=30
def solve():
    p5 = [n**5 for n in range(10)]
    lim = 6 * p5[9]
    total = 0

    for n in range(2, lim + 1):
        if n == sum(p5[int(d)] for d in str(n)):
            total += n

    return total

if __name__ == "__main__":
    print(solve())