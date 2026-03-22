# Problem 38: https://projecteuler.net/problem=38
def solve():
    best = 0

    for n in range(9123, 9877):
        s = f"{n}{2 * n}"
        if len(s) == 9 and set(s) == set("123456789"):
            best = max(best, int(s))

    return best

if __name__ == "__main__":
    print(solve())