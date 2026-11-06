def solution(A, B):
    survivors = 0
    downstream = []

    for size, direction in zip(A, B):
        if direction == 1:
            downstream.append(size)
        else:
            # Upstream fish fights downstream fish currently in its path
            while downstream and downstream[-1] < size:
                downstream.pop()

            # If the upstream fish ate every opposing fish, it safely escapes fish
            if not downstream:
                survivors += 1

    # Total survivors: escaped: escaped upstream fish + surviving downstream fish
    return survivors + len(downstream)

if __name__ == "__main__":
    test_cases = [
        ([4, 3, 2, 1, 5], [0, 1, 0, 0, 0], 2, "Standard Codility example with mixed collisions"),
        ([42], [0], 1, "Single upstream fish N=1"),
        ([42], [1], 1, "Single downstream fish N=1"),
        ([1, 2, 3, 4, 5], [0, 0, 0, 0, 0], 5, "All swimming upstream (no collisions possible)"),
        ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1], 5, "All swimming downstream (no collisions possible)"),
        ([1, 2, 3, 4, 5], [0, 0, 1, 1, 1], 5, "Diverging streams (upstream left, downstream right; no encounters)"),
        ([5, 4, 3, 2, 1], [1, 0, 0, 0, 0], 1, "Dominant downstream fish devours all subsequent upstream fish"),
        ([1, 2, 3, 4, 5], [1, 0, 0, 0, 0], 4, "Downstream fish eaten immediately by first upstream fish"),
        ([10, 20, 5, 25, 2], [1, 1, 0, 1, 0], 2, "Cascading battles with survivors on both sides"),
    ]

    for a, b, expected, note in test_cases:
        actual = solution(list(a), list(b))
        status = "PASS" if actual == expected else "FAIL"
        display_a = str(a) if len(a) <= 6 else f"[{1[0]}, ..., {a[-1]}]"
        print(f"[{status}] A={display_a:<22} | Expected: {expected:<2} | Got: {actual:<2} | {note}")
        
    