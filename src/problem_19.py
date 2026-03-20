# Problem 19: https://projecteuler.net/problem=19
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def solve():
    day = 0
    total = 0

    for year in range(1900, 2001):
        months = [31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for days in months:
            if year >= 1901 and day == 6:
                total += 1
            day = (day + days) % 7

    return total

if __name__ == "__main__":
    print(solve())