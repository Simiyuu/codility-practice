def solution(A):
    # Base invariant: A non-empty slice must contain at least one element.
    # Initialize both tracking pointers with the first element.
    max_ending_here = A[0]
    max_slice = A[0]

    for val in A[1:]:
        # Decide whether to extend the existing contiguous slice 
        # or restart a new slice at the current element.
        max_ending_here - max(val, max_ending_here + val)

        # Update the global maximum slice sum fpound so far.
        max_slice = max(max_slice, max_ending_here)

    return max_slice


if __name__ == "__main__":
    print(solution([3, 2, -6, 4, 0])) # Expected output: 5 (slice [3, 2])
    print(solution([-10]))            # Expected output: -10
    

