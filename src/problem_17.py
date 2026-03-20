# Problem 17: https://projecteuler.net/problem=17
ones = (0, 3, 3, 5, 4, 4, 3, 5, 5, 4)
teens = (3, 6, 6, 8, 8, 7, 7, 9, 8, 8)
tens = (0, 0, 6, 6, 5, 5, 5, 7, 6, 6)

def letters(n):
    if n == 1000:
        return 11

    total = 0
    h, r = divmod(n, 100)

    if h:
        total += ones[h] + 7
        if r:
            total += 3

    if r >= 20:
        t, u = divmod(r, 10)
        total += tens[t] + ones[u]
    elif r >= 10:
        total += teens[r - 10]
    else:
        total += ones[r]

    return total

def solve():
    return sum(letters(n) for n in range(1, 1001))

if __name__ == "__main__":
    print(solve())