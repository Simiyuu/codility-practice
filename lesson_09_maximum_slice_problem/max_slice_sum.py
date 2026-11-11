def solution(A):
    max_ending_here = A[0]
    max_slice = A[0]

    for val in A[1:]:
        max_ending_here = max(val, max_ending_here + val)
        max_slice = max(max_slice, max_ending_here)

    return max_slice

if __name__ == "__main__":
    test_cases = [
        ([3, 2, -6, 4, 0], 5, "Standard Codlity example (slice [3, 2])"),
        ([-10], -10, "Single negative element N=1"),
        ([10], -10, "Single positive element N=1"),
        ([-5, -2, -8, -1, -4], -1, "All negative elements (must select least negative)"),
        ([1, 2, 3, 4], 10, " All positive elements (entire array slice)"),
        ([1, -2, 3, -1, 4, -3], 6, "Alternating signs (optimal slice [3, -1, 4])"),
        ([0, 0, 0], 0, "All zero array"),
        ([-3, 5], 5, "Two elements: negative followed by positive"),
        ([-7, -3], -3, "Two negative elements"),
        ([5, -10, 8], 8, "Deep middle dip breaking slice continuity"),
        ([-1_000_000, 1_000_000, -1_000_000], 1_000_000, "Maximum constarint extreme values"),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "Classic LeetCode 53 subarray case ([4, -1, 2, 1])"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 28 else f"{str(arr[:2])[:-1]}...{str(arr[-1:])[1:]}"
        print(f"[{status}] A={display_arr:<28} | Expected: {expected:<9} | Got: {actual:<9} | {note}")
        
