def solution(A):
    n = len(A)
    if n == 0:
        return 0

    i = 0
    j = n - 1
    distinct_count = 0
    last_val = None

    while i <= j:
        left_val = abs(A[i])
        right_val = abs(A[j])

        # Pick the larger absolute value and move the respective pointer inward
        if left_val >= right_val:
            val = left_val
            i += 1
        else:
            val = right_val
            j -= 1

        # Count the value if it differs from the last processed absolute value
        if val != last_val:
            distinct_count += 1
            last_val = val

    return distinct_count

if __name__ == "__main__":
    print(solution([-5, -3, -1, 0, 3, 6]))  # Expected output: 5 (abs values: 5, 3, 1, 0, 6)
    print(solution([-5, -2, -1, 0, 1, 3]))  # Expected output: 4 (abs values: 5, 2, 1, 0, 3)
    