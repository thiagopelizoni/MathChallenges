# Problem 185: https://projecteuler.net/problem=185
from itertools import combinations
from math import comb

BITS = tuple(1 << d for d in range(10))
ALL = (1 << 10) - 1

CLUES = (
    ("5616185650518293", 2),
    ("3847439647293047", 1),
    ("5855462940810587", 3),
    ("9742855507068353", 3),
    ("4296849643607543", 3),
    ("3174248439465858", 1),
    ("4513559094146117", 2),
    ("7890971548908067", 3),
    ("8157356344118483", 1),
    ("2615250744386899", 2),
    ("8690095851526254", 3),
    ("6375711915077050", 1),
    ("6913859173121360", 1),
    ("6442889055042768", 2),
    ("2321386104303845", 0),
    ("2326509471271448", 2),
    ("5251583379644322", 2),
    ("1748270476758276", 3),
    ("4895722652190306", 1),
    ("3041631117224635", 3),
    ("1841236454324589", 3),
    ("2659862637316867", 2),
)


def clue_state(domains, guess, target):
    forced = []
    optional = []

    for i, d in enumerate(guess):
        bit = BITS[d]
        if domains[i] & bit:
            if domains[i] == bit:
                forced.append(i)
            else:
                optional.append(i)

    need = target - len(forced)
    if 0 <= need <= len(optional):
        return forced, optional, need
    return None


def restrict(domains, guess, forced, chosen):
    out = list(domains)
    matched = set(forced)
    matched.update(chosen)

    for i, d in enumerate(guess):
        bit = BITS[d]
        if i in matched:
            if not out[i] & bit:
                return None
            out[i] = bit
        elif out[i] & bit:
            out[i] ^= bit
            if not out[i]:
                return None

    return tuple(out)


def search(domains, clues, remaining):
    if not remaining:
        if all(d.bit_count() == 1 for d in domains):
            return "".join(str(d.bit_length() - 1) for d in domains)
        return None

    best = None
    best_state = None
    best_score = None

    for idx in remaining:
        state = clue_state(domains, *clues[idx])
        if state is None:
            return None
        _, optional, need = state
        score = (comb(len(optional), need), len(optional))
        if best_score is None or score < best_score:
            best = idx
            best_state = state
            best_score = score

    guess, _ = clues[best]
    forced, optional, need = best_state
    rest = tuple(i for i in remaining if i != best)

    for chosen in combinations(optional, need):
        narrowed = restrict(domains, guess, forced, chosen)
        if narrowed is None:
            continue
        if any(clue_state(narrowed, *clues[i]) is None for i in rest):
            continue
        found = search(narrowed, clues, rest)
        if found is not None:
            return found

    return None


def solve():
    clues = [(tuple(map(int, guess)), count) for guess, count in CLUES]
    zero = next(guess for guess, count in clues if count == 0)
    domains = tuple(ALL ^ BITS[d] for d in zero)
    active = tuple((guess, count) for guess, count in clues if count)
    return search(domains, active, tuple(range(len(active))))


if __name__ == "__main__":
    print(solve())
