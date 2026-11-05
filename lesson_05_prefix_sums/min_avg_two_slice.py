def solution(A):
    min_avg = float("inf")
    min_idx = 0

    for i in range(len(A) - 1):
        # Check slice of length 2: A[i .. i + 1]
        avg_2 = (A[i] + A[i + 1]) / 2.0
        if avg_2 < min_avg:
            min_avg = avg_2
            min_idx = i

        # Check slice of length 3: A[i .. i + 2]
        if i < len(A) - 2:
            avg_3 = (A[i] + A[i + 1] + A[i + 2]) / 3.0
            if avg_3 < min_avg:
                min_avg = avg_3
                min_idx = i

    return min_idx


if __name__ == "__main__":
    test_cases = [
        ([4, 2, 2, 5, 1, 5, 8], 1, "Standard Codility example (slice [2, 2] has avg 2.0)"),
        ([1, 2], 0, "Minimal array size N=2"),
        ([5, 6, 1, 4, 1, 7], 2, "Length-3 slice strictly optimal ([1, 4, 1] avg=2.0 vs len-2 avgs=2.5)"),
        ([-3, -5, -8, -4, -10], 2, "All negative numbers (slice [-8, -4, -10] avg=-7.33 vs [-8, -4] avg=-6.0)"),
        ([10, -10, 10, -10], 0, "Alternating signs testing tie-breaking at index 0"),
        ([2, 2, 2, 2], 0, "All identical values returning earliest index"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] A={str(arr):<26} | Expected: {expected:<2} | Got: {actual:<2} | {note}")
        

