# Problem 701: https://projecteuler.net/problem=701

import numpy as np


def expectation(w, h):
    base = w * h + 1
    dp = {(0,) * w: (np.array([0], dtype=np.int64), np.array([1], dtype=np.int64))}

    for cell in range(w * h):
        col = cell % w
        pending = {}
        for frontier, (keys, counts) in dp.items():
            sizes = [keys // base ** i % base for i in range(1, max(frontier) + 1)]
            for black in (False, True):
                labels = list(frontier)
                largest = keys % base
                if black:
                    above = labels[col]
                    left = labels[col - 1] if col else 0
                    joined = set((above, left)) - {0}
                    area = np.ones_like(keys)
                    for label in joined:
                        area += sizes[label - 1]
                    new = len(sizes) + 1
                    labels = [new if label in joined else label for label in labels]
                    labels[col] = new
                    largest = np.maximum(largest, area)
                else:
                    labels[col] = 0

                order = list(dict.fromkeys(label for label in labels if label))
                names = {label: i + 1 for i, label in enumerate(order)}
                frontier_new = tuple(names.get(label, 0) for label in labels)
                encoded = largest.copy()
                for i, label in enumerate(order, 1):
                    size = area if black and label == new else sizes[label - 1]
                    encoded += size * base ** i
                pending.setdefault(frontier_new, []).append((encoded, counts))

        dp = {}
        for frontier, parts in pending.items():
            keys = np.concatenate([part[0] for part in parts])
            counts = np.concatenate([part[1] for part in parts])
            keys, inverse = np.unique(keys, return_inverse=True)
            totals = np.zeros(len(keys), dtype=np.int64)
            np.add.at(totals, inverse, counts)
            dp[frontier] = keys, totals

    total = sum(int(np.dot(keys % base, counts)) for keys, counts in dp.values())
    return total / 2 ** (w * h)


def solve():
    return f"{expectation(7, 7):.8f}"


if __name__ == "__main__":
    print(solve())
