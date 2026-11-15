# Problem 749: https://projecteuler.net/problem=749


def solve(d=16):
    limit = 10**d
    found = set()
    counts = [0] * 10
    k = 2

    while 2**k <= limit:
        powers = [digit**k for digit in range(10)]

        def search(digit, left, total, digit_sum):
            if digit == 1:
                for delta in (-1, 1):
                    if (total + delta - digit_sum) % 9:
                        continue
                    for ones in range(left + 1):
                        n = total + ones + delta
                        if not 0 < n < limit:
                            continue
                        counts[0] = left - ones
                        counts[1] = ones
                        s = str(n).zfill(d)
                        if counts == [s.count(c) for c in "0123456789"]:
                            found.add(n)
                return

            power = powers[digit]
            bound = min(left, (limit - total) // power)
            for count in range(bound + 1):
                counts[digit] = count
                search(digit - 1, left - count, total + count * power,
                       digit_sum + count * digit)

        search(9, d, 0, 0)
        k += 2

    return sum(found)


if __name__ == "__main__":
    print(solve())
