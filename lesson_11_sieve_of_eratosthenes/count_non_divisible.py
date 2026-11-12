def solution(A):
    n = len(A)
    max_val = max(A)

    # 1. Count occurrences of each element in A
    freq = [0] * (max_val + 1)
    for val in A:
        freq[val] += 1

    # 2. Sieve through multiples to count how many elements in A divide each number 
    divisor_counts = [0] * (max_val + 1)
    for x in range(1, max_val + 1):
        if freq[x] > 0:
            for multiple in range(x, max_val + 1, x):
                divisor_counts[multiple] += freq[x]


    # 3. Subtract total divisors from N to get non-divisors for each position
    return [n - divisor_counts[val] for val in A]

if __name__ == "__main__":
    print(solution([3, 1, 2, 3, 6]))  # Expected output: [2, 4, 3, 2, 0]
    print(solution([1, 1, 1]))        # Expected output: [0, 0, 0]