def solution(A):
    total_sum = sum(A)
    left_sum = 0
    min_diff = float("inf")

    # Iterate up to len(A) - 1 so both left and right sides are non-empty
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total_sum - left_sum
        diff = abs(left_sum - right_sum)
        if diff < min_diff:
            min_diff = diff
            if min_diff == 0:
                return 0

    return min_diff

if __name__ == "__main__":
    test_cases = [
        ([3, 1, 2, 4, 3], 1, "Standard example split (|7 - 6| = 1)"),
        ([3, 10], 7, "Minimal two-element array (|3 - 10| = 7)"),
        ([-1000, 1000], 2000, "Negative to positive extreme (|-1000 - 1000| = 2000)"),
        ([1, 1], 0, "Identical two-element split"),
        ([5, 2, 7, 10], 4, "Split occurs near the right boundary"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] A={str(arr):<25} | Expected: {expected:<5} | Got: {actual:<5} | {note}")

        