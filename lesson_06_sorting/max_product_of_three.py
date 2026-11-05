def solution(A):
    A.sort()

    # Candidates 1: The three largest elements
    cand_1 = A[-1] * A[-2] * A[-3]

    # Candidate 2: The two most negative elements multiplied by the largest element
    cand_2 = A[0] * A[1] * A[-2]

    return max(cand_1, cand_2)

if __name__ == "__main__":
    print(solution([-3, 1, 2, -2, 5, 6])) # Expected output: 60 (from 2 * 5 * 6)

    