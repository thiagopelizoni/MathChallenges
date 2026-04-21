# Problem 85: https://projecteuler.net/problem=85

def solve():
    target = 2_000_000
    best_diff = target
    best_area = 0

    for m in range(1, 200):
        a = m * (m + 1) // 2
        for n in range(m, 200):
            b = n * (n + 1) // 2
            cnt = a * b
            diff = abs(cnt - target)
            if diff < best_diff:
                best_diff = diff
                best_area = m * n
            if cnt > target and cnt - target > best_diff:
                break

    return best_area


if __name__ == "__main__":
    print(solve())
