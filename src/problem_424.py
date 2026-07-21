# Problem 424: https://projecteuler.net/problem=424

from itertools import permutations
import re
from urllib.request import urlopen


URL = "https://projecteuler.net/resources/documents/0424_kakuro200.txt"
PERMUTATIONS = {
    n: tuple(permutations(range(1, 10), n)) for n in range(1, 7)
}


def candidates(run, clue):
    variables = tuple(dict.fromkeys(run + tuple(ord(c) - 65 for c in clue)))
    result = []
    for digits in PERMUTATIONS[len(run)]:
        total = sum(digits)
        if len(clue) == 1:
            if total >= 10:
                continue
            clue_digits = (total,)
        else:
            if total < 10:
                continue
            clue_digits = divmod(total, 10)

        values = {}
        for var, digit in zip(run, digits):
            if var in values and values[var] != digit:
                break
            values[var] = digit
        else:
            for letter, digit in zip(clue, clue_digits):
                var = ord(letter) - 65
                if var in values and values[var] != digit:
                    break
                values[var] = digit
            else:
                letters = [values[var] for var in values if var < 10]
                if len(letters) == len(set(letters)):
                    result.append(tuple(values[var] for var in variables))
    return variables, result


def make_problem(line):
    parts = []
    token = []
    depth = 0
    for char in line:
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        if char == "," and depth == 0:
            parts.append("".join(token))
            token = []
        else:
            token.append(char)
    parts.append("".join(token))
    size = int(parts[0])
    cells = parts[1:]
    cell_vars = {}
    domains = [set(range(10)) for _ in range(10)]
    next_var = 10

    for pos, cell in enumerate(cells):
        if cell == "O":
            cell_vars[pos] = next_var
            domains.append(set(range(1, 10)))
            next_var += 1
        elif len(cell) == 1 and "A" <= cell <= "J":
            var = ord(cell) - 65
            cell_vars[pos] = var
            domains[var].discard(0)

    constraints = []
    for pos, cell in enumerate(cells):
        if not cell.startswith("("):
            continue
        row, _ = divmod(pos, size)
        for direction, clue in re.findall(r"([hv])([A-J]+)", cell):
            step = 1 if direction == "h" else size
            run = []
            q = pos + step
            while q in cell_vars and (direction == "v" or q // size == row):
                run.append(cell_vars[q])
                q += step
            if len(clue) == 2:
                domains[ord(clue[0]) - 65].discard(0)
            constraints.append(candidates(tuple(run), clue))
    return domains, constraints


def propagate(domains, constraints):
    while True:
        changed = False
        singles = [next(iter(domains[i])) for i in range(10) if len(domains[i]) == 1]
        if len(singles) != len(set(singles)):
            return None
        assigned = set(singles)

        for i in range(10):
            if len(domains[i]) > 1:
                reduced = domains[i] - assigned
                if not reduced:
                    return None
                if reduced != domains[i]:
                    domains[i] = reduced
                    changed = True

        for digit in range(10):
            places = [i for i in range(10) if digit in domains[i]]
            if not places:
                return None
            if len(places) == 1 and len(domains[places[0]]) > 1:
                domains[places[0]] = {digit}
                changed = True

        reduced_constraints = []
        for variables, options in constraints:
            valid = [
                option
                for option in options
                if all(
                    value in domains[var]
                    for var, value in zip(variables, option)
                )
            ]
            if not valid:
                return None
            for j, var in enumerate(variables):
                reduced = domains[var].intersection(option[j] for option in valid)
                if not reduced:
                    return None
                if reduced != domains[var]:
                    domains[var] = reduced
                    changed = True
            reduced_constraints.append((variables, valid))
        constraints = reduced_constraints

        if not changed:
            return domains, constraints


def search(domains, constraints):
    state = propagate([set(domain) for domain in domains], constraints)
    if state is None:
        return None
    domains, constraints = state
    undecided = [i for i, domain in enumerate(domains) if len(domain) > 1]
    if not undecided:
        return domains

    var = min(undecided, key=lambda i: len(domains[i]))
    for value in sorted(domains[var]):
        child = [set(domain) for domain in domains]
        child[var] = {value}
        result = search(child, constraints)
        if result is not None:
            return result
    return None


def solve_puzzle(line):
    domains, constraints = make_problem(line)
    result = search(domains, constraints)
    return int("".join(str(next(iter(result[i]))) for i in range(10)))


def solve():
    lines = urlopen(URL, timeout=20).read().decode().splitlines()
    return sum(solve_puzzle(line) for line in lines)


if __name__ == "__main__":
    print(solve())
