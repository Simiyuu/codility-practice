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
    print(solution([4, 3, 4, 4, 4, 2])) # Expected output: 2 (indices S=0 and S=2)
    print(solution([1, 2, 3, 4, 5]))    # Expected output: 0
    