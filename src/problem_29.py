# Problem 29: https://projecteuler.net/problem=29
def solve():
    terms = {a**b for a in range(2, 101) for b in range(2, 101)}
    return len(terms)

if __name__ == "__main__":
    print(solve())