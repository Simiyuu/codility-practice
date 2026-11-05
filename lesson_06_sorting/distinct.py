def solution(A):
    if not A:
        return 0

    A.sort()
    distinct_count = 1

    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            distinct_count += 1

    return distinct_count

if __name__ == "__main__":
    test_cases = [
        ([2, 1, 1, 2, 3, 1], 3, "Standard Codility example with mixed duplicates"),
        ([], 0, "Empty array boundary N=0"),
        ([42], 1, "Single element N=1"),
        ([5, 5, 5, 5, 5], 1, "All Identical elements"),
        ([1, 2, 3, 4, 5], 5, "All unique consecutive elements"),
        ([-10, 0, 10, -10, 0], 3, "Mixed negative zero, and positive values"),
        ([-1_000_000, 1_000_000, -1_000_000], 2, "Extreme value boundaries [-10^6, 10^6]"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(list(arr))
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(arr) <= 8 else f"[{arr[0]}, ..., {arr[-1]}] (len={len(arr)})"
        print(f"[{status}] A={display_arr:<25} | Expected: {expected:<2} | Got: {actual:<2} | {note}")
