def solution(A):
    n = len(A)
    # A triplet (X, Y, Z) requires N >= 3. For N = 3, both slices ae empty (sum = 0).
    if n < 4:
        return 0

    # max_ending_here[i]: maximunm slice sum ending strictly at index i
    # Floored at 0 because a slice can be empty (yeilding sum 0)
    max_ending_here = [0] * n
    for i in range(1, n - 1):
        max_ending_here[i] = max(0, max_ending_here[i - 1] + A[i])

    # max_starting_here[i]: maximum slice sum strictly at index i
    # Floored at 0 because a slice can be empty
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
    print(solution([3, 2, 6, -1, 4, 5, -1, 2])) # Expected output: 17 (X=0, Y=3, Z=7 -> slices [2,6] and [4,5])
    print(solution([5, 17, 0, 3]))              # Expected output: 17 (X=0. Y=2, z=3 -> slice [17])
