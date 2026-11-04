def solution(A, B, K):
    divisibles_up_to_B = B // K
    divisibles_up_to_A = A // K
    inclusive_boundary_offset = 1 if A % K == 0 else 0

    return divisibles_up_to_B - divisibles_up_to_A + inclusive_boundary_offset

if __name__ == "__main__":
    print(solution(6, 11, 2)) # Expected output: 3 (divisibles: 6, 8, 10)

    