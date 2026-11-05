def solution(S, P, Q):
    n = len(S)
    # Pre-allocate prefix sum tables of length n + 1 with 0-based boundary padding
    pref_a = [0] * (n + 1)
    pref_c = [0] * (n + 1)
    pref_g = [0] * (n + 1)

    for i, char in enumerate(S):
        pref_a[i + 1] = pref_a[i] + (1 if char == "A" else 0)
        pref_c[i + 1] = pref_c[i] + (1 if char == "C" else 0)
        pref_g[i + 1] = pref_g[i] + (1 if char == "G" else 0)

    result = []
    for start, end in zip(P, Q):
        # Range count for [start .. end] is pref[end + 1] = pref[start]
        if pref_a[end + 1] - pref_a[start] > 0:
            result.append(1)
        elif pref_c[end + 1] - pref_c[start] > 0:
            result.append(2)
        elif pref_g[end + 1] - pref_g[start] > 0:
            result.append(3)
        else:
            result.append(4)

    return result

if __name__ == "__main__":
    test_cases = [
        ("CAGCCTA", [2, 5, 0], [4, 5, 6], [2, 4, 1], "Standard Codility example with mixed slices"),
        ("ACGT", [0, 1, 2, 3], [0, 1, 2, 3], [1, 2, 3, 4], "Single-nucleotide slices testing each impact factor directly"),
        ("T", [0], [0], [4], "Single-element string with highest impact factor (T=4)"),
        ("A", [0], [0], [1], "Single-element string with lowest impact factor (A=1)"),
        ("TTTTTT", [0, 2], [5, 4], [4, 4], "Homogeneous sequence containing only T"),
        ("GGGGGG", [1, 0], [3, 5], [3, 3], "Homogeneous sequence containing only G"),
        ("CCCCAA", [0, 2], [3, 5], [2, 1], "Slices checking boundary transition from C to A"),
        ("TCGATCGA", [0, 4], [7, 7], [1, 1], "Full and partial spans spanning all 4 nucleotides"),
    ]

    for s, p, q, expected, note in test_cases:
        actual = solution(s, p, q)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] S={s:<10} | P={str(p):<12} | Q={str(q):<12} | Expected: {expected} | Got: {actual} | {note}")
        
