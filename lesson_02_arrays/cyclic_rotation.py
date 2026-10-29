def solution(A, K):
    # Guard clause empty array or single-element array needs no rotation
    if not A or len(A) <= 1:
        return A
    
    # Optimize K: rotating len(A) times brings array needs no rotation
    n = len(A)
    k = K % n

    # If effective rotation is zero , array is unchanged
    if k == 0:
        return A

    # Slice and concatenate: last k elements + elements before last k
    return A[-k:] + A[:-k]

if __name__ == "__main__":
    test_cases = [
        # Standard rotations
        ([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]),
        ([0, 0, 0], 1, [0, 0 ,0]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
        # Edge cases
        ([], 5, []), # Empty array
        ([1], 99, [1]), # Single element, K > N
        ([1, 2], 3, [2, 1]), # K > N (3 % 2 = 1 shift)
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]), # K = 0
        ([-1, -2, -3, -4], 2, [-3, -4, -1, -2]) # Negative integers
    ]

    for idx, (arr, shifts, expected) in enumerate(test_cases, 1):
        result = solution(arr, shifts)
        assert result == expected, f"Test {idx} Failed: Expected {expected}, got {result}"
        print(f"Test {idx} Passed: {arr} rotated by {shifts} -> {result}")
        
    print("\nAll CyclicRotation test cases passed successfully.")
    

