def solution(A):
    n = len(A)
    if n < 3:
        return 0

    A.sort()
    traingles = 0

    for p in range(n -2):
        r = p + 2
        for q in range(p + 1, n - 1):
            # Advance r as far right as the triangle inequality holds
            while r < n and A[p] + A[q] > A[r]:
                r += 1
            # All indices between q + 1 and r - 1 from valid triangles with p and q
            traingles += (r - q - 1)

    return traingles

if __name__ == "__main__":
    test_cases = [
        ([10, 2, 5, 1, 8, 12], 4, "Standard Codility example"),
        ([], 0, "Empty array N=0"),
        ([5], 0, "Single element N=1"),
        ([3, 4], 0, "Two elements N=2"),
        ([2, 2, 2, 2], 4, "All identical elements (4 choose 3)"),
        ([1, 2, 10], 0, "Impossible traingle inequality"),
        ([0, 0, 0], 0, "All zeros"),
        ([1, 1, 1], 1, "Minimum boundary N=3 valid traingle"),
        ([10, 5, 6, 8, 20], 3, "Mixed sequence with multiple traingles"),
        ([1000000000, 1000000000, 1000000000], 1, "Max constraint scale elements"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(list(arr))
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 22 else f"[len={len(arr)}]"
        print(f"[{status}] A={display_arr:<22} | Expected: {expected:<5} | Got: {actual:<5} | {note}")

        