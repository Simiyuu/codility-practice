def solution(A):
    n = len(A)
    if n < 2:
        return 0

    # Phase 1: Boyer-Moore Voting to find candidate
    candidate = None
    count = 0
    for val in A:
        if count == 0:
            candidate = val
            count = 1
        elif val == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: Count total occurrences of candidate
    total_leader_count = 0
    for val in A:
        if val == candidate:
            total_leader_count += 1

    # If the candidate is not a dominator of the whole array,
    # no equi leaders can exist.
    if total_leader_count <= n // 2:
        return 0

    leader = candidate
    equi_leaders = 0
    left_leader_count = 0

    # Phase 3: Single-pass split scan across 0 <= S < N - 1
    for S in range(n - 1):
        if A[S] == leader:
            left_leader_count += 1

        right_leader_count = total_leader_count - left_leader_count
        left_len = S + 1
        right_len = n - left_len

        # Check if the overall leader dominates both sub-slices
        if (left_leader_count > left_len // 2) and (right_leader_count > right_len // 2):
            equi_leaders += 1

    return equi_leaders

if __name__ == "__main__":
    test_cases = [
        ([4, 3, 4, 4, 4, 2], 2, "Standard Codility example (splits at S=0 and S=2)"),
        ([1, 2, 3, 4, 5], 0, "No global leader exists"),
        ([4], 0, "Single element boundary N=1 (requires N >= 2 for split)"),
        ([4, 4], 1, "Two identical element N=2 (singlevalid split at S=0)"),
        ([1, 2], 0, "Two distinct elements N=2 (no majority on either side)"),
        ([5, 5, 5, 5, 5], 4, "Homogeneous array of length 5 (all 4 splits valid)"),
        ([2, 1, 1, 3, 1], 0, "Global leader 1 exists (3/5), but zero valid equi-splits"),
        ([1, 2, 1, 2, 1, 2], 0, "Even length alternating pattern with no majority"),
        ([-2147483648, -2147483648, -2147483648, 10], 1, "Extreme negative 32-bit integer with single valid split"),
        ([-1, -1], 1, "Two negative identical elements"),
        ([0, 0, 0, 1, 0, 0], 4, "Heavy leader majority with multiple valid partitions"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 28 else f"{str(arr[:2])[:-1]}...{str(arr[-1:])[1:]}"
        print(f"[{status}] A={display_arr:<28} | Expected: {expected:<2} | Got: {actual:<2} | {note}")
