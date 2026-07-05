# Problem 361: https://projecteuler.net/problem=361

from functools import lru_cache


MOD = 10**9
LAST_POWER = 18
WORDS = {
    1: ("1",),
    2: ("10", "11"),
    3: ("100", "101", "110"),
}


@lru_cache(maxsize=None)
def count_words(length):
    if length <= 3:
        return length

    half = length // 2
    if length % 2 == 0:
        return count_words(half) + count_words(half + 1)
    return 2 * count_words(half + 1)


@lru_cache(maxsize=None)
def count_prefix(length):
    if length <= 0:
        return 0
    if length <= 3:
        return length * (length + 1) // 2

    half = length // 2
    if length % 2 == 0:
        return 3 * count_prefix(half) + count_prefix(half + 1) - 4
    return count_prefix(length - 1) + 2 * count_words(half + 1)


def length_for_index(index):
    lo = 1
    hi = 1
    while count_prefix(hi) < index:
        hi *= 2

    while lo < hi:
        mid = (lo + hi) // 2
        if count_prefix(mid) >= index:
            hi = mid
        else:
            lo = mid + 1
    return lo


class Node:
    __slots__ = ("kind", "child", "length", "text")

    def __init__(self, kind, child, length, text=None):
        self.kind = kind
        self.child = child
        self.length = length
        self.text = text


EMPTY = Node("literal", None, 0, "")


def literal(text):
    return Node("literal", None, len(text), text)


def complement(child):
    if child.length == 0:
        return child
    return Node("complement", child, child.length)


def even_start(child, length):
    return Node("even_start", child, length)


def odd_start(child, length):
    return Node("odd_start", child, length)


@lru_cache(maxsize=None)
def first_digit(node):
    if node.kind == "literal":
        return int(node.text[0])
    if node.kind == "complement":
        return 1 - first_digit(node.child)
    if node.kind == "even_start":
        return first_digit(node.child)
    return 1 - first_digit(node.child)


@lru_cache(maxsize=None)
def last_digit(node):
    if node.kind == "literal":
        return int(node.text[-1])
    if node.kind == "complement":
        return 1 - last_digit(node.child)
    if node.kind == "even_start":
        if node.length % 2 == 0:
            return 1 - last_digit(node.child)
        return last_digit(node.child)
    if node.length % 2 == 0:
        return last_digit(node.child)
    return 1 - last_digit(node.child)


@lru_cache(maxsize=None)
def drop_first(node):
    if node.length == 0:
        return node
    if node.length == 1:
        return EMPTY
    if node.kind == "literal":
        return literal(node.text[1:])
    if node.kind == "complement":
        return complement(drop_first(node.child))
    if node.kind == "even_start":
        return odd_start(node.child, node.length - 1)
    return even_start(drop_first(node.child), node.length - 1)


@lru_cache(maxsize=None)
def drop_last(node):
    if node.length == 0:
        return node
    if node.length == 1:
        return EMPTY
    if node.kind == "literal":
        return literal(node.text[:-1])
    if node.kind == "complement":
        return complement(drop_last(node.child))
    if node.kind == "even_start":
        if node.length % 2 == 0:
            return even_start(node.child, node.length - 1)
        return even_start(drop_last(node.child), node.length - 1)
    if node.length % 2 == 0:
        return odd_start(drop_last(node.child), node.length - 1)
    return odd_start(node.child, node.length - 1)


def max_depth(length):
    depth = 0
    while length > 3:
        length = length // 2 + 1
        depth += 1
    return depth


def eval_depth():
    length = max(length_for_index(10**k) for k in range(1, LAST_POWER + 1))
    return max_depth(length) + 3


LEVELS = eval_depth()
BASES = tuple(pow(2, 2**k, MOD) for k in range(LEVELS))


@lru_cache(maxsize=None)
def power_base(level, exponent):
    return pow(BASES[level], exponent, MOD)


@lru_cache(maxsize=None)
def geom_sum(base, count):
    if count == 0:
        return 0
    if count == 1:
        return 1
    if count % 2 == 0:
        half = geom_sum(base, count // 2)
        return (half + pow(base, count // 2, MOD) * half) % MOD
    return (geom_sum(base, count - 1) + pow(base, count - 1, MOD)) % MOD


@lru_cache(maxsize=None)
def morph_evals(node):
    base_values = evals(node)
    values = []
    for level, base in enumerate(BASES):
        if level + 1 >= LEVELS:
            values.append(0)
            continue
        squared = base * base % MOD
        val = (base - 1) * base_values[level + 1]
        val += geom_sum(squared, node.length)
        values.append(val % MOD)
    return tuple(values)


@lru_cache(maxsize=None)
def evals(node):
    if node.length == 0:
        return (0,) * LEVELS

    if node.kind == "literal":
        values = []
        for base in BASES:
            val = 0
            for ch in node.text:
                val = (val * base + int(ch)) % MOD
            values.append(val)
        return tuple(values)

    if node.kind == "complement":
        child_values = evals(node.child)
        return tuple(
            (geom_sum(base, node.length) - child_values[level]) % MOD
            for level, base in enumerate(BASES)
        )

    if node.kind == "even_start":
        if node.length % 2 == 0:
            return morph_evals(node.child)

        prefix = drop_last(node.child)
        last = last_digit(node.child)
        prefix_values = morph_evals(prefix)
        return tuple(
            (prefix_values[level] * base + last) % MOD
            for level, base in enumerate(BASES)
        )

    half = node.length // 2
    first = first_digit(node.child)
    last = last_digit(node.child)
    if node.length % 2 == 1:
        tail_values = morph_evals(drop_first(node.child))
        return tuple(
            ((1 - first) * power_base(level, 2 * half) + tail_values[level])
            % MOD
            for level in range(LEVELS)
        )

    mid_values = morph_evals(drop_last(drop_first(node.child)))
    return tuple(
        (
            (1 - first) * power_base(level, 2 * half - 1)
            + mid_values[level] * BASES[level]
            + last
        )
        % MOD
        for level in range(LEVELS)
    )


@lru_cache(maxsize=None)
def kth_word(length, rank, start):
    if start == 0:
        total = count_words(length)
        return complement(kth_word(length, total - 1 - rank, 1))

    if length <= 3:
        return literal(WORDS[length][rank])

    even_length = (length + 1) // 2
    even_count = count_words(even_length)
    if rank < even_count:
        return even_start(kth_word(even_length, rank, 1), length)

    odd_length = length // 2 + 1
    return odd_start(kth_word(odd_length, rank - even_count, 0), length)


def value_mod(index):
    if index == 0:
        return 0

    length = length_for_index(index)
    rank = index - count_prefix(length - 1) - 1
    return evals(kth_word(length, rank, 1))[0]


def solve():
    return sum(value_mod(10**k) for k in range(1, LAST_POWER + 1)) % MOD


if __name__ == "__main__":
    print(solve())
