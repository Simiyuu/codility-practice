def solution(A):
    n = len(A)
    if n == 0:
        return 0

    i = 0
    j = n - 1
    distinct_count = 0
    last_val = None

    while i <= j:
        left_val = abs(A[i])
        right_val = abs(A[j])

        # Pick the larger absolute value and move the respective pointer inward
        if left_val >= right_val:
            val = left_val
            i += 1
        else:
            val = right_val
            j -= 1

        # Count the value if it differs from the last processed absolute value
        if val != last_val:
            distinct_count += 1
            last_val = val

    return distinct_count

if __name__ == "__main__":
    test_cases = [
        ([-5, -3, -1, 0, 3, 6], 5, "Standard Codility example (abs: 5, 3, 1, 0, 6)"),
        ([-5, -2, -1, 0, 1, 3], 5, "Mixed negatives and positives with duplicate magnitude 1"),
        ([7], 1, "Minimum boundary N=1 single positive element"),
        ([-7], 1, "Minimum boundary N=1 single negative element"),
        ([0], 1, "Minimum boundary N=1 single zero"),
        ([0, 0, 0, 0], 1, "All zeros"),
        ([4, 4, 4, 4], 1, "All identical positive elements"),
        ([-4, -4, -4, -4], 1, "All identical negative elements"),
        ([-5, -5, -2, 2, 5, 5], 2, "Symmetric negative/positive duplicates"),
        ([-10, -7, -3, -1], 4, "Strictly negative sorted array"),
        ([1, 3, 7, 10], 4, "Strictly positive sorted array"),
        ([-2_147_483_648, -1, 0, 1, 2_147_483_647], 4, "32-bit signed integer min/max extremes"),
        ([-2_147_483_648, -2_147_483_648], 1, "Duplicate 32-bit signed integer minimum"),
        (list(range(-50_000, 50_000)), 50_001, "Max constraint boundary N=100,000 spanning -50_000..49,999"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 26 else f"[len={len(arr)}]"
        print(f"[{status}] A={display_arr:<26} | Expected: {expected:<6} | Got: {actual:<6} | {note}")
        
        