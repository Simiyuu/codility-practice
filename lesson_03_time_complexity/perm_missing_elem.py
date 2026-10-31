def solution(A):
    n = len(A)
    # The full range contains numbers from 1 to n + 1
    total_count = n + 1
    expected_sum = total_count * (total_count + 1) // 2
    actual_sum = sum(A)

    return expected_sum - actual_sum

if __name__ == "__main__":
    test_cases = [
        ([2, 3, 1, 5], 4, "Standard unsorted permutation"),
        ([2, 3, 4, 5], 1, "Missing the very first element (1)"),
        ([1, 2, 3, 4,], 5, "Missing the very last element (N + 1)"),
        ([], 1, "Empty array (N=0, sequence is [1], missing 1)"),
        ([2], 1, "Single-element array missing 1"),
        ([1], 2, "Single-element array missing 2"),
        ([1, 3], 2, "Two elements missing middle value"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] A={str(arr):<20} | Expected: {expected:<3} | Got: {actual:<3} | {note}")
        