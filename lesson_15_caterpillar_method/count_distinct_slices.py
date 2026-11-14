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
    test_cases = [
        (6, [3, 4, 5, 5, 2], 9, "Standard Codility example"),
        (5, [3], 1, "Minimum boundary N=1 single element"),
        (5, [1, 2, 3, 4], 10, "All unique elements (N(N+1)/2 = 10)"),
        (3, [2, 2, 2, 2], 4, "All identical elements"),
        (2, [0, 1, 0, 1], 7, "Alternating elements"),
        (0, [0, 0, 0], 3, "All zeros with M=0"),
        (10, [5, 5, 1, 2, 5], 8, "Duplicates forcing contractions"),
        (100, list(range(100)), 5050, "Medium sequence of 100 unique elements"),
        (10, [1] * 50_000, 50_000, "Large N=50,000 array with identical elements"),
        (100_000, list(range(50_000)), 1_000_000_000, "Max constraints N=50,000 unique elements triggering 1B cap"),
    ]

    for m_val, arr, expected, note in test_cases:
        actual = solution(m_val, arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 22 else f"[len={len(arr)}]"
        print(f"[{status}] M={m_val:<6} A={display_arr:<22} | Expected: {expected:<13} | Got: {actual:<13} | {note}")

        