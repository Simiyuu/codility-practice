def solution(A):
    A.sort()

    # Candidates 1: The three largest elements
    cand_1 = A[-1] * A[-2] * A[-3]

    # Candidate 2: The two most negative elements multiplied by the largest element
    cand_2 = A[0] * A[1] * A[-2]

    return max(cand_1, cand_2)

if __name__ == "__main__":
    test_cases = [
        ([-3, 1, 2, -2, 5, 6], 60, "Standard Codility example (2 * 5 * 6)"),
        ([-5, 5, -5, 4], 125, "Two negatives outperform three largest ((-5) * (-5) * 5)"),
        ([-10, -10, 1, 2, 5], 500, "Large negatives dominating: (-10) * (-10) * 5 vs 1 * 2 * 5"),
        ([-5, -6, -4, -7, -10], -120, "All negative elements (least negative triplet: (-6) * (-5) * (-4))"),
        ([10, 10, 10], 1000, "Minimal constraint array N=3 with identical values"),
        ([-10, 0, 0, 1, 2], 0, "Zero boundary absorption"),
        ([-1000, 1000, -1000, 1000], 1_000_000_000, "Extreme value bounds [-1000, 1000] maximizing product"),
    ]

    for arr, expected, note in test_cases:
        # Pass a shallow copy so the original test case array isn't mutated in the output
        actual = solution(list(arr))
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(arr) <= 6 else f"[{arr[0]}, ..., {arr[-1]}]"
        print(f"[{status}] A={display_arr:<26} | Expected: {expected:<11} | Got: {actual:<11} | {note}")
