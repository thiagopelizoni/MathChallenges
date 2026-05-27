# Problem 265: https://projecteuler.net/problem=265


N = 5


def solve():
    m = 1 << N
    mask = m - 1
    bits = [0] * N
    seen = {0}
    total = 0

    def closes(cur):
        for b in bits[: N - 1]:
            cur = ((cur << 1) & mask) | b
            if cur in seen:
                return False
        return True

    def value():
        n = 0
        for b in bits:
            n = (n << 1) | b
        return n

    def search(cur):
        nonlocal total

        if len(bits) == m:
            if closes(cur):
                total += value()
            return

        for b in (0, 1):
            nxt = ((cur << 1) & mask) | b
            if nxt not in seen:
                seen.add(nxt)
                bits.append(b)
                search(nxt)
                bits.pop()
                seen.remove(nxt)

    search(0)
    return total


if __name__ == "__main__":
    print(solve())
