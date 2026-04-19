# Problem 79: https://projecteuler.net/problem=79

from collections import defaultdict

def solve():
    data = [
        "319", "680", "180", "690", "129", "620", "762", "689", "762", "318",
        "368", "710", "720", "710", "629", "168", "160", "689", "716", "731",
        "736", "729", "316", "729", "729", "710", "769", "290", "719", "680",
        "318", "389", "162", "289", "162", "718", "729", "319", "790", "680",
        "890", "362", "319", "760", "316", "729", "380", "319", "728", "716"
    ]
    
    nodes = set("".join(data))
    edges = defaultdict(set)
    for log in data:
        edges[log[0]].add(log[1])
        edges[log[1]].add(log[2])
    
    # Simple topological sort for a DAG where the solution is unique
    res = []
    remaining = sorted(list(nodes))
    while remaining:
        for char in remaining:
            # Check if any other remaining char must come before this one
            if all(char not in edges[other] for other in remaining if other != char):
                res.append(char)
                remaining.remove(char)
                break
    
    return "".join(res)

if __name__ == "__main__":
    print(solve())
