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
    # next_peak[i] stores the index of the first peak at or after index i
    next_peak = [-1] * n 
    for p in peaks:
        next_peak[p] = p 

    for i in range(n - 2, -1, -1):
        if next_peak[i] == -1:
            next_peak[i] = next_peak[i + 1]

    # 3. Upper bound on K: (K - 1) * K <= peaks[-1] - peaks[0]
    max_k = min(num_peaks, math.isqrt(peaks[-1] - peaks[0]) + 1)

    # 4. Greedy verification from max_k downward
    for K in range(max_k, 0, -1):
        flags_used = 1
        pos = peaks[0]

        while flags_used < K:
            pos += K
            if pos >= n or next_peak[pos] == -1:
                break
            pos = next_peak[pos]
            flags_used += 1

        if flags_used == K:
            return K
    
    return 0


if __name__ == "__main__":
    print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])) # Expected output: 3 (peaks at 1, 3, 5, 10)
    print(solution([1, 3, 1]))
    
