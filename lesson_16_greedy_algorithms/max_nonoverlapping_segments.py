def solution(A, B):
    n = len(A)
    if n == 0:
        return 0

    count = 1
    prev_end = B[0]

    for i in range(1, n):
        # If the current segment starts strictly after the previous selected segment ends
        if A[i] > prev_end:
            count += 1
            prev_end = B[i]

    return count

if __name__ == "__main__":
    test_cases = [
        ([1, 3, 7, 9, 9], [5, 6, 8, 9, 10], 3, "Standard Codility example"),
        ([], [], 0, "Empty arrays N=0"),
        ([1], [5], 1, "Single segment N=1"),
        ([1, 2, 3], [4, 5, 6], 1, "Fully overlapping segments starting at different points"),
        ([1, 6, 11], [5, 10, 15], 3, "Completed disjoint segments"),
        ([1, 2, 3], [2, 3, 4], 1, "Chained adjacent touching segments"),
        ([10, 1, 5], [15, 3, 8], 2, "Unsorted or mixed segment order"), 
    ]

    for a_arr, b_arr, expected, note in test_cases:
        actual = solution(a_arr, b_arr)
        status = "PASS" if actual == expected else "FAIL"
        display_a = str(a_arr) if len(str(a_arr)) <= 18 else f"[len={len(a_arr)}]"
        print(f"[{status}] A={display_a:<18} | Expected: {expected:<2} | Got: {actual:<2} | {note}")

        