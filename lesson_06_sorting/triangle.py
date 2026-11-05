def solution(A):
    if len(A) < 3:
        return 0
    
    A.sort()

    for i in range(len(A) - 2):
        # In a sorted array, A[i+2] >= A[i+1] >= A[i].
        # If A[i] + A[i+1] > A[i+2], all three traingle conditions are satisfied.
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0

if __name__ == "__main__":
    print(solution([10, 2, 5, 1, 8, 20])) # Expected output: 1 (triplet 5, 8, 10)
    print(solution([10, 50, 5, 1]))       # Expected output: 0