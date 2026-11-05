def solution(A):
    if not A:
        return 0

    A.sort()
    distinct_count = 1

    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            distinct_count += 1

    return distinct_count

if __name__ == "__main__":
    print(solution([2, 1, 1, 2, 3, 1])) # Expected output: 3
    