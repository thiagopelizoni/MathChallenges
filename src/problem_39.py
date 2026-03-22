# Problem 39: https://projecteuler.net/problem=39
def solve():
    best_p = 0
    best_count = 0

    for p in range(2, 1001, 2):
        count = 0

        for a in range(1, p // 3):
            num = p * (p - 2 * a)
            den = 2 * (p - a)
            if num % den:
                continue

            b = num // den
            if a < b:
                count += 1

        if count > best_count:
            best_count = count
            best_p = p

    return best_p

if __name__ == "__main__":
    print(solve())