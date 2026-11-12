import math

def solution(A):
    n = len(A)
    if n < 3:
        return 0

    # 1. Identify all peak indices: A[i-1] < A[i] > A[i+1]
    peaks = []
    for i in range(1, n - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks.append(i)


    num_peaks = len(peaks)
    if num_peaks <= 1:
        return num_peaks
    
    # 2. Precompute next_peak array for 0(1) jump lookups
    # next_peaks[i] stores the index of the first peak at or after index i
    next_peak = [-1] * n  
    for p in peaks:
        next_peak[p] = p 

    for i in range(n - 2, -1, -1):
        if next_peak[i] == -1:
            next_peak[i] == next_peak[i + 1]

    # 3. Upper bound on K: (K - 1) * K <= peaks[-1] - peaks[0]
    max_k = min(num_peaks, math.isqrt(peaks[-1] - peaks[0]) + 1)

    # 4. Greedy verification from max_k downward
    for K in range(max_k, 0, -1):
        flags_used = 1
        pos = peaks[0]

        while flags_used < K:
            pos += max_k
            if pos >= n or next_peak[pos] == -1:
                break
            pos = next_peak[pos]
            flags_used += 1

        if flags_used == K:
            return max_k
        
    return 0


if __name__ == "__main__":
    test_cases = [
        ([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2], 3, "Standard Codility example (peaks at 1, 3, 5, 10)"),
        ([1, 3, 1], 1, "Minimal sigle peak array N=3"),
        ([], 0, "Empty array boundary N=0"),
        ([5], 0, "Single element boundary N=1"),
        ([1, 2], 0, "Two elements boundary N=2 (no interior index)"),
        ([1, 2, 3, 4, 5], 0, "Strictly increasing slope (no peaks)"),
        ([5, 4, 3, 2, 1], 0, "Strictly decreasing slope (no peaks)"),
        ([2, 2, 2, 2, 2], 0, "Flat plateau (strict inequality required)"),
        ([1, 3, 3, 1], 0, "Double flat top (neither index stictly greater than both neighbors)"),
        ([0, 1, 0, 1, 0], 2, "Two peaks spaced exactly distance 2 apart"),
        ([0, 1, 0, 1, 0, 1, 0], 2, "Three tightly packed peaks (distance 2, max flags 2)"),
        ([0, 1, 0, 0, 1, 0, 0, 1, 0, ], 3, "Three peaks spaced exactly distance 3 apart"),
        ([0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0], 4, "Four peaks spaced distance 4 apart"),
    ]

    for arr, expected, note in test_cases:
        actual = solution(arr)
        status = "PASS" if actual == expected else "FAIL"
        display_arr = str(arr) if len(str(arr)) <= 28 else f"{str(arr[:2])[:-1]}...{str(arr[-1:])[1:]}"
        print(f"[{status}] A={display_arr:<28} | Expected: {expected:<2} | Got: {actual:<2} | {note}")
        