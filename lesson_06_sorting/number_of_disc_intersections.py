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
    print(solution([1, 5, 2, 1, 4, 0])) # Expected output: 11
    
    