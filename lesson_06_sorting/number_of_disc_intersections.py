def solution(A):
    n = len(A)
    if n < 2:
        return 0

    starts = [i - A[i] for i in range(n)]
    ends = [i + A[i] for i in range(n)]

    starts.sort()
    ends.sort()

    intersections = 0
    end_idx = 0

    for start_idx in range(n):
        # Advance end_idx past all discs that closed strictly before the current disc opened
        while end_idx < n and ends[end_idx] < starts[start_idx]:
            end_idx += 1

        # The current disc intersects with all currently open active  discs (excluding itself)
        intersections += start_idx - end_idx

        if intersections > 10_000_000:
            return -1

    return intersections

if __name__ == "__main__":
    max_radius = 2_147_483_647
    test_cases = [
        ([1, 5, 2, 1, 4, 0], 11, "Standard Codility example with mixed radius overlap"),
        ([], 0, "Empty array boundary N=0"),
        ([10], 0, "Single disc N=1 (pairs require at least 2 discs)"),
        ([0, 0, 0, 0], 0, "Zero-radius point discs with no shared coordinate boundaries"),
        ([1, 0, 1], 3, "Tnagent contact points touching exactly at boundary coordinate 1"),
        ([max_radius, max_radius], 1, "Extreme 32-bit signed radius bounds without overflow"),
        ([10_000] * 5_000, -1, "Exceeding the 10,000,000 limit (5000 discs completely overlapping = 12,497,500 pairs)"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(list(arr))
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(arr) <= 6 else f"[{arr[0]}, ..., {arr[-1]}] (len={len(arr)})"
        print(f"[{status}] A={display_arr:<25} | Expected: {expected:<2} | Got: {actual:<2} | {note }")

        
    