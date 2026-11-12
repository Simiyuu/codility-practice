def solution(A):
    n = len(A)
    max_val = max(A)

    # 1. Count occurrences of each element in A
    freq = [0] * (max_val + 1)
    for val in A:
        freq[val] += 1

    # 2. Sieve through multiples to count how many element in A divide each number
    divisor_counts = [0] * (max_val + 1)
    for x in range(1, max_val + 1):
        if freq[x] > 0:
            for multiple in range(x, max_val + 1, x):
                divisor_counts[multiple] += freq[x]

    # 3. Subtract total divisors from N to get non-divisors for each position
    return [n - divisor_counts[val] for val in A]

if __name__ == "__main__":
    test_cases = [
        ([3, 1, 2, 3, 6], [2, 4, 3, 2, 0], "Standard Codility example"),
        ([1], [0], "Minimum boundary N=1 with value 1"),
        ([2], [0], "Minimum boundary N=1 with max value 2N=2"),
        ([1, 1, 1], [0, 0, 0], "All ones (1 divides every element)"),
        ([5, 5, 5, 5], [0, 0, 0, 0], "All identical composite/prime elements"),
        ([2, 3, 5, 7], [3, 3, 3, 3], "Distinct primes with 1 (each divided only by itself)"),
        ([1, 2, 3, 5, 7], [4, 3, 3, 3, 3], "Distinct primes with 1 included"),
        ([1, 2, 4, 8], [3, 2, 1, 0], "Ascending powers of 2 divisibility chain"),
        ([8, 4, 2, 1], [0, 1, 2, 3], "Descending powers of 2 divisibility chain"),
        ([10, 5, 2, 1, 3], [1, 3, 3, 4, 3], "Upper value constraint boundary A[i] = 2N"),
        ([6, 6, 3, 3, 2, 2], [0, 0, 4, 4, 4, 4], "Repeated multiple and prime factors"),
        ([12, 4, 6, 8, 3, 1], [1, 4, 3, 3, 4, 5], "Overlapping composite divisors"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 24 else f"{str(arr[:2])[:1]}...{str(arr[-1:])[1:]}"
        print(f"[{status}] A={display_arr:<24} | Expected: {str(expected):<20} | Got: {str(actual):<20} | {note}")
        