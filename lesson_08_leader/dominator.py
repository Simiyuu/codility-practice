def solution(A):
    if not A:
        return -1

    candidate = None
    count = 0
    candidate_index = -1

    # Phase 1: Boyer-Moore Voting Algorithm (Pairwise Elimination)
    for i, val in enumerate(A):
        if count == 0:
            candidate = val
            candidate_index = 1
            count = 1
        elif val == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: Verification Pass
    actual_count = 0
    for val in A:
        if val == candidate:
            actual_count += 1

    # Strict majority condition: count > floor(N / 2)
    if actual_count > len(A) // 2:
        return candidate_index

    return -1

if __name__ == "__main__":
    # Test cases defined as: (Array, Expected Value or None, Note)
    # Codility accepts ANY valid index where the dominator appears.
    test_cases = [
        ([3, 4, 3, 2, 3, -1, 3, 3], 3, "Codility example (dominator 3 occurs 5/8 times)"),
        ([1, 2, 3, 4, 5], None, "No dominator (all unique elements)"),
        ([], None, "Empty array boundary N=0"),
        ([42], 42, "Single element array N=1"),
        ([7, 7], 7, "Two identical elements (2/2 occurrences)"),
        ([1, 2], None, "Two distinct elements (exact 50% split, no majority)"),
        ([1, 2, 1, 2], None, "Even length with tie (2/4 occurrences, not > 2)"),
        ([0, 0, 0, 1, 1], 0, "Dominator at the beginning of array"),
        ([1, 1, 0, 0, 0], 0, "Dominator at the end of array"),
        ([-2147483648, -2147483648, 2147483647], -2147483648, "Extreme 32-bit signed integer values"),
        ([9, 9, 9, 9, 9], 9, "Homogeneous array of identical values"),
    ]

    for arr, expected_val, note in test_cases:
        actual_index = solution(arr)

        if expected_val is None:
            # Expected -1 because no dominator exists
            passed = actual_index == -1
            result_str = f"Got: {actual_index}"
        else:
            # Expecting a valid index where A[index] == expected_val
            passed = (
                actual_index != -1
                and 0 <= actual_index < len(arr)
                and arr[actual_index] == expected_val
            )
            val_at_index = arr[actual_index] if (0 <= actual_index <len(arr)) else "N/A"
            result_str = f"Index: {actual_index} (A[{actual_index}]={val_at_index})"

        status = "PASS" if passed else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 24 else f"{str(arr[:2])[:-1]}...{str(arr[-1:])[1:]}"
        print(f"[{status}] A={display_arr:<24} | Expected Val: {str(expected_val):<12} | {result_str:<28} | {note}")
        
    