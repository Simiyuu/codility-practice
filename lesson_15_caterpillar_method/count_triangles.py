def solution(A):
    n = len(A)
    if n < 3:
        return 0

    A.sort()
    triangles = 0

    for p in range(n - 2):
        r = p + 2
        for q in range(p + 1, n - 1):
            # Advance r as far right as the triangle inequality holds
            while r < n and A[p] + A[q] > A[r]:
                r += 1
            # All indices between q + 1 and r - 1 form valid triangles with p and q
            triangles += (r - q - 1)

    return triangles

if __name__ == "__main__":
    print(solution([10, 2, 5, 1, 8, 12]))  # Expected output: 4 (triplets: (2, 5, 8), (2, 8, 10), (5, 8, 10), (8, 10, 12))

