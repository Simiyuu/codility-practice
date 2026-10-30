def rotate_right(A, K):
    if not A or len(A) <= 1:
        return A

    n = len(A)
    k = K % n

    if k == 0:
        return A

    return A[-k:] + A[:-k]

if __name__ == "__main__":
    print("\n--- Testing CyclicRotation Edge Cases ---")
    rotation_cases = [
        ([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8], "Standard multi-element shift"),
        ([0, 0, 0], 1, [0, 0, 0], "Identical values"),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4], "Full cycle (K == len(A))"),
        ([], 5, [], "Empty array (avoids ZeroDivisionError)"),
        ([42], 99, [42], "Single element with large K"),
        ([1, 2], 3, [2, 1], "K greater than length (3 % 2 == 1)"),
        ([10, 20, 30], 0, [10, 20, 30], "Zero shifts (K == 0)"),
        ([-1, -2, -3, -4], 2, [-3, -4, -1, -2], "Negative integer preservation"),
    ]

    for arr, k, expected, note in rotation_cases:
        actual = rotate_right(arr, k)
        status = "PASS" if actual == expected else "FAIL"
        print(f"[{status}] A={str(arr):<20} | K={k:<2} | Expected: {str(expected):<20} | Got: {str(actual):<20} | {note}")
        

