def solution(A):
    if len(A) < 3:
        return 0
    
    A.sort()

    for i in range(len(A) - 2):
        # In a sorted array, A[i+2] >= A[i+1] >= A[i].
        # If A[i] + A[i+1] > A[i+2], all three traingle conditions are satisfied.
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0

if __name__ == "__main__":
    max_int = 2_147_483_647
    test_cases = [
        ([10, 2, 5, 1, 8, 20], 1, "Standard Codility example with valid triplet (5, 8, 10)"),
        ([10, 50, 5, 1], 0, "Standard Codility negative example with no valid triplet"),
        ([], 0, "Empty array boundary N=0"),
        ([1, 2], 0, "Under minimum size N=2"),
        ([5, 5, 5], 1, "Equilateral triplet with identical values"),
        ([1, 1, 2, 3, 5, 8], 0, "Fibonacci sequence: adjacent sums equal next value (A[i]+A[i+1] == A[i+2])"),
        ([-5, -4, -3, -2, -1], 0, "All negative values: negative lengths cannot form geometric traingles"),
        ([-10, -5, 1, 2, 4], 0, "Mixed negative and positive with failing positive triplet (1 + 2 < 4)"),
        ([max_int -2, max_int - 1, max_int], 1, "Extreme 32-bit signed integer boundary near 2^31 - 1"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(list(arr))
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(arr) <= 6 else f"[{arr[0]}, ..., {arr[-1]}] (len={len(arr)})"
        print(f"[{status}] A={display_arr:<25} | Expected: {expected} | Got: {actual} | {note}")

        