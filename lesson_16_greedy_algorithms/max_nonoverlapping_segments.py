def solution(A, B):
    n = len(A)
    if n == 0:
        return 0

    count = 1
    prev_end = B[0]

    for i in range(1, n):
        # If the current segment starts strictly after the previous selected segments ends
        if A[i] > prev_end:
            count += 1
            prev_end = B[i]

        return count

if __name__ == "__main__":
    print(solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]))  # Expected output: 3
    print(solution([1], [5]))                              # Expected output: 1
    