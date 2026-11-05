def solution(A):
    min_avg = float("inf")
    min_idx = 0

    for i in range(len(A) - 1):
        # Check slice of length 2: A[i .. i + 1]
        avg_2 = (A[i] + A[i + 1]) / 2.0
        if avg_2 < min_avg:
            min_avg = avg_2
            min_idx = i

        # Check slice of length 3: A[i .. i + 2]
        if i < len(A) - 2:
            avg_3 = (A[i] + A[i + 1] + A[i + 2]) / 3.0
            if avg_3 < min_avg:
                min_avg = avg_3
                min_idx = i

    return min_idx


if __name__ == "__main__":
    print(solution([4, 2, 2, 5, 1, 5, 8])) # Expected output: 1 (slice [2, 2] has avg 2.0)

