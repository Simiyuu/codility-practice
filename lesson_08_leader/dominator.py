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
    print(solution([3, 4, 3, 2, 3, -1, 3, 3])) # Expected output: 0, 2, 4, 6, or 7
    print(solution([1, 2, 3, 4, 5]))           # Expected output: -1
    