def solution(A):
    n = len(A)
    # A triplet (X, Y, Z) requires N >= 3. For N = 3, both slices are empty (sum = 0).
    if n < 4:
        return 0

    # max_ending_here[i]: maximum slice sum sum ending strictly at index i
    # Floored at 0 because an empty slice yields a sum of 0
    max_ending_here = [0] * n 
    for i in range(1, n - 1):
        max_ending_here[i] = max(0, max_ending_here[i - 1] + A[i])

    # max_starting_here[i]: maximum slice sum starting strictly at index i
    # Floored at 0  because an empty slice yields a sum of 0
    max_starting_here = [0] * n 
    for i in range(n - 2, 0, -1):
        max_starting_here[i] = max(0, max_starting_here[i + 1] + A[i])

    # Evaluate all possible center split points Y (1 <= Y <= N - 2)
    max_double_slice = 0
    for Y in range(1, n - 1):
        current_sum = max_ending_here[Y - 1] + max_starting_here[Y + 1]
        if current_sum > max_double_slice:
            max_double_slice = current_sum
    
    return max_double_slice

if __name__ == "__main__":
    test_cases = [
        ([3, 2, 6, -1, 4, 5, -1, 2], 17, "Standard Codility example (slices [2, 6] and [4, 5])"),
        ([5, 17, 0, 3], 17, "Four-element minimal slice (X=0, Y=2, Z=3 -> slice [17])"),
        ([1, 2, 3], 0, "Array of length 3 (boundary condition, both slices empty)"),
        ([1, 2, 3, 4, 5], 7, "All positive values (X=0, Y=1, Z=4 -> empty left, [3, 4] right)"),
        ([-3, -5, -1, -4, -2], 0, "All negative values (both slices empty, floored to 0)"),
        ([0, 10, -5, -2, 0], 10, "Negative valley flanked by posiitve slice (X=0, Y=2, Z=3)"),
        ([6, 1, 5, 6, 4, 2, 9, 4], 26, "Subarray sum optimization across wide split"),
        ([-10, 0, 0, 0, 10], 0, "Zero interior elements"),
        ([10, -100, 10, -100, 10], 10, "Heavy negative alternating bloackers"),
        ([-10000, 10000, 10000, 10000, -10000], 20000, "Maximum constraint values with interior positive blocks"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 28 else f"{str(arr[:2])[:-1]}...{str(arr[-1:])[1:]}"
        print(f"[{status}] A={display_arr:<28} | Expected: {expected:<5} | Got: {actual:<5} | {note}")
        