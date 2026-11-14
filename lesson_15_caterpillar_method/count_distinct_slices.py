def solution(M, A):
    n = len(A)
    back = 0
    front = 0
    total_slices = 0
    seen = [False] * (M + 1)

    while back < n:
        # Expand the caterpillar front as far as elements remain distinct
        while front < n and not seen[A[front]]:
            seen[A[front]] = True
            front += 1

        # All sub-slices starting at 'back' and ending from 'back' to 'front - 1' are unique
        total_slices += (front - back)
        if total_slices >= 1_000_000_000:
            return 1_000_000_000

        # Contract the caterpillar from the back, removing A[back] from seen
        seen[A[back]] = False
        back += 1

    return total_slices

if __name__ == "__main__":
    print(solution(6, [3, 4, 5, 5, 2])) # Expected ouput: 9 (slices: (0.0), (0, 1), (0,2), (1,1), (1,2), (2,2), (3,3), (3,4), (4,4))
    